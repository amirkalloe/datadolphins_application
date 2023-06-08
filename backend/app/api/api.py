from fastapi import APIRouter

from app.api.endpoints import gebruiker

router = APIRouter()
router.include_router(gebruiker.router, prefix="/gebruikers", tags=["Gebruiker"])
