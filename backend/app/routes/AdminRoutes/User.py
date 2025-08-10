from fastapi import APIRouter

router= APIRouter(prefix="/userAdmin",tags=["Admin User"])

@router.get("/")
async def root():
    return {
        "message":"Welcome to Admin User Home "
    }