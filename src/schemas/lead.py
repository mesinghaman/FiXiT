from typing import List
from pydantic import BaseModel


class LeadIn(BaseModel):
    lead_id: str
    source: str
    budget: float
    city: str
    property_type: str
    last_activity_minutes_ago: int
    past_interactions: int
    notes: str
    status: str


class LeadOut(BaseModel):
    lead_id: str
    priority_score: float
    priority_bucket: str
    reasons: List[str]
