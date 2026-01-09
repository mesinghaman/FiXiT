from fastapi import APIRouter
from src.schemas.call import CallEvalIn, CallEvalOut
from src.core.call_scoring import run_call_eval

router = APIRouter()


@router.post("/call-eval", response_model=CallEvalOut)
def call_eval(payload: CallEvalIn) -> CallEvalOut:
    return run_call_eval(payload)
