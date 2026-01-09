import json
import os
from typing import Literal

import requests


Intent = Literal["urgent", "soft", "none"]

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")


def classify_note_intent(note: str) -> Intent:
    """
    Uses an OSS LLM (Ollama) to classify lead intent from notes.
    Output is constrained to keep scoring deterministic.
    """

    prompt = (
        "Classify the intent of the following real-estate lead note.\n"
        "Respond with exactly one word from this list:\n"
        "urgent, soft, none\n\n"
        f"Note: {note}"
    )

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "format": "json",
    }

    try:
        resp = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json=payload,
            timeout=8,
        )
        resp.raise_for_status()

        raw = resp.json().get("response", "").strip().lower()

        if raw in {"urgent", "soft", "none"}:
            return raw 

    except Exception:
        pass

  
    txt = note.lower()
    if any(k in txt for k in ["urgent", "asap", "this week", "immediately"]):
        return "urgent"
    if any(k in txt for k in ["looking", "checking", "maybe", "exploring"]):
        return "soft"

    return "none"
