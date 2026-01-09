from pydantic import BaseModel
from typing import Dict


class CallEvalIn(BaseModel):
    call_id: str
    lead_id: str
    transcript: str
    duration_seconds: int


class CallEvalOut(BaseModel):
    quality_score: float
    labels: Dict[str, bool]
    summary: str
    next_actions: str
    model_metadata: Dict[str, float | str]
