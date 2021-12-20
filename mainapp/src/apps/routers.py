from fastapi import APIRouter

from src.apps.edvora.endpoints import edvora_assignment
api_router = APIRouter()
api_router.include_router(edvora_assignment, prefix='/edvora', tags=["edvora"])

