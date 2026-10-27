"""Provider layer. Stdlib only (urllib), so nothing extra to install.

Select the backend in this order (first hit wins):
  1. the `provider` argument to get_provider()
  2. the LLM_PROVIDER environment variable
  3. config/llm.json ("provider")
  4. default: "anthropic"

Backends:
  anthropic  Anthropic Messages API   needs ANTHROPIC_API_KEY
  ollama     Ollama local server      needs `ollama serve` running (default http://localhost:11434)
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from pathlib import Path
from typing import Protocol

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config" / "llm.json"
ANTHROPIC_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_VERSION = "2023-06-01"


class LLMError(RuntimeError):
    pass


def load_config(path: Path = CONFIG_PATH) -> dict:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def _post(url: str, payload: dict, headers: dict, timeout: float) -> dict:
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", **headers},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise LLMError(f"HTTP {e.code} from {url}: {e.read().decode('utf-8', 'replace')}") from e
    except urllib.error.URLError as e:
        raise LLMError(f"cannot reach {url}: {e.reason}") from e


class Provider(Protocol):
    name: str

    def complete(self, system: str, messages: list[dict], max_tokens: int) -> str: ...


class AnthropicProvider:
    name = "anthropic"

    def __init__(self, model: str, api_key: str | None = None, timeout: float = 120):
        self.model = model
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY", "")
        self.timeout = timeout
        if not self.api_key:
            raise LLMError("ANTHROPIC_API_KEY is not set")

    def complete(self, system: str, messages: list[dict], max_tokens: int) -> str:
        payload = {"model": self.model, "max_tokens": max_tokens, "messages": messages}
        if system:
            payload["system"] = system
        data = _post(
            ANTHROPIC_URL,
            payload,
            {"x-api-key": self.api_key, "anthropic-version": ANTHROPIC_VERSION},
            self.timeout,
        )
        return "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")


class OllamaProvider:
    name = "ollama"

    def __init__(self, model: str, host: str | None = None, timeout: float = 300):
        self.model = model
        self.host = (host or os.environ.get("OLLAMA_HOST") or "http://localhost:11434").rstrip("/")
        self.timeout = timeout

    def complete(self, system: str, messages: list[dict], max_tokens: int) -> str:
        msgs = ([{"role": "system", "content": system}] if system else []) + messages
        payload = {
            "model": self.model,
            "messages": msgs,
            "stream": False,
            "options": {"num_predict": max_tokens},
        }
        data = _post(f"{self.host}/api/chat", payload, {}, self.timeout)
        try:
            return data["message"]["content"]
        except (KeyError, TypeError) as e:
            raise LLMError(f"unexpected Ollama response: {data}") from e


def get_provider(provider: str | None = None, config: dict | None = None) -> Provider:
    cfg = load_config() if config is None else config
    name = (provider or os.environ.get("LLM_PROVIDER") or cfg.get("provider") or "anthropic").lower()

    if name == "anthropic":
        a = cfg.get("anthropic", {})
        model = os.environ.get("ANTHROPIC_MODEL") or a.get("model", "claude-haiku-5-5")
        return AnthropicProvider(model=model, timeout=a.get("timeout", 120))
    if name == "ollama":
        o = cfg.get("ollama", {})
        model = os.environ.get("OLLAMA_MODEL") or o.get("model", "llama3.1")
        host = os.environ.get("OLLAMA_HOST") or o.get("host")
        return OllamaProvider(model=model, host=host, timeout=o.get("timeout", 300))
    raise LLMError(f"unknown provider '{name}' (use 'anthropic' or 'ollama')")


def complete(prompt: str, system: str = "", provider: str | None = None, max_tokens: int = 1024) -> str:
    """One-shot helper: send a single user prompt, get the text back."""
    p = get_provider(provider)
    return p.complete(system, [{"role": "user", "content": prompt}], max_tokens)
