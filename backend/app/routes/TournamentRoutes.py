from fastapi import APIRouter

router= APIRouter(prefix="/tournaments",tags=["Tournament"])

@router.get("/")
async def root():
    return {
        "message":"Welcome to TournamentRouteHome"
    }