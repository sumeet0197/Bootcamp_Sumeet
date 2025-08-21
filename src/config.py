from __future__ import annotations
import os
from dataclasses import dataclass
from dotenv import load_dotenv

@dataclass
class Paths:
    raw: str
    processed: str

def load_env() -> Paths:
    """Load environment and return data directories."""
    load_dotenv()
    raw = os.getenv("DATA_DIR_RAW", "data/raw")
    processed = os.getenv("DATA_DIR_PROCESSED", "data/processed")
    os.makedirs(raw, exist_ok=True)
    os.makedirs(processed, exist_ok=True)
    return Paths(raw=raw, processed=processed)

def get_key(name: str, default: str | None = None) -> str | None:
    """Return env var (e.g., API keys)."""
    return os.getenv(name, default)
