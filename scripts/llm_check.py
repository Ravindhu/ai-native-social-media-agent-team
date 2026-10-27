#!/usr/bin/env python3
"""Ping the configured LLM backend.

Usage:
  python3 scripts/llm_check.py                    # uses config/llm.json or LLM_PROVIDER
  python3 scripts/llm_check.py --provider ollama  # force a backend
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from llm import get_provider  # noqa: E402
from llm.providers import LLMError  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", choices=["anthropic", "ollama"])
    ap.add_argument("--prompt", default="Reply with the single word: ready")
    args = ap.parse_args()
    try:
        p = get_provider(args.provider)
        print(f"provider={p.name} model={p.model}")
        print(p.complete("", [{"role": "user", "content": args.prompt}], 32).strip())
        return 0
    except LLMError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
