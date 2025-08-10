from fastapi import APIRouter

router= APIRouter(prefix="/games",tags=["Games"])

@router.get("/")
async def root():
    return {
        "message":"Welcome to GameRouteHome"
    }