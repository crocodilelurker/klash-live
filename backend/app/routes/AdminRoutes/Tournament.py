from fastapi import APIRouter

router= APIRouter(prefix="/tournamentAdmin",tags=["Admin Tournament"])

@router.get("/")
async def root():
    return {
        "message":"Welcome to Admin Tournament Home"
    }