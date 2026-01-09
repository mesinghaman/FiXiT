from typing import List

from fastapi import APIRouter

from app.schemas.lead import LeadIn, LeadOut
from app.core.lead_scoring import score_lead

router = APIRouter()


@router.post("/lead-priority", response_model=List[LeadOut])
def lead_priority(leads: List[LeadIn], max_results: int = 5) -> List[LeadOut]:
    ranked = [score_lead(l) for l in leads]
    ranked.sort(key=lambda x: x.priority_score, reverse=True)
    return ranked[:max_results]
