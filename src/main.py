from fastapi import FastAPI

from src.api.lead_priority import router as lead_router
from src.api.call_eval import router as call_router

app = FastAPI(title="FiXiT")

app.include_router(lead_router)
app.include_router(call_router)
