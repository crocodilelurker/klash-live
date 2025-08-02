from fastapi import APIRouter

router= APIRouter(prefix="/users",tags=["Users"])

@router.get("/")
async def root():
    return {
        "message":"Welcome to UserRouteHome"
    }