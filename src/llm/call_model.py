import json
import os
import time

import requests


OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")


def analyze_call(text: str) -> dict:
    prompt = (
        "Analyze this real-estate sales call transcript.\n"
        "Return strict JSON with:\n"
        "quality_score (0 to 1),\n"
        "labels {rapport_building, need_discovery, closing_attempt, compliance_risk},\n"
        "summary,\n"
        "next_actions.\n\n"
        f"Transcript:\n{text}"
    )

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "format": "json",
    }

    for _ in range(2):   
        try:
            res = requests.post(
                f"{OLLAMA_URL}/api/generate",
                json=payload,
                timeout=10,
            )
            res.raise_for_status()

            raw = json.loads(res.json().get("response", "{}"))

            return {
                "quality_score": float(raw.get("quality_score", 0.0)),
                "labels": {
                    "rapport_building": bool(
                        raw.get("labels", {}).get("rapport_building", False)
                    ),
                    "need_discovery": bool(
                        raw.get("labels", {}).get("need_discovery", False)
                    ),
                    "closing_attempt": bool(
                        raw.get("labels", {}).get("closing_attempt", False)
                    ),
                    "compliance_risk": bool(
                        raw.get("labels", {}).get("compliance_risk", False)
                    ),
                },
                "summary": raw.get("summary", ""),
                "next_actions": raw.get("next_actions", ""),
                "model": OLLAMA_MODEL,
            }

        except Exception:
            time.sleep(0.5)

 
    return {
        "quality_score": 0.3,
        "labels": {
            "rapport_building": False,
            "need_discovery": False,
            "closing_attempt": False,
            "compliance_risk": False,
        },
        "summary": "Model unavailable, fallback result.",
        "next_actions": "Review call manually.",
        "model": OLLAMA_MODEL,
    }
