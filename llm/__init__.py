"""LLM provider layer: one call signature, two backends (Anthropic API or Ollama)."""
from .providers import complete, get_provider, load_config

__all__ = ["complete", "get_provider", "load_config"]
