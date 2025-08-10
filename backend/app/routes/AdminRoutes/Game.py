from fastapi import APIRouter

router= APIRouter(prefix="/gameAdmin",tags=["Admin Game"])

@router.get("/")
async def root():
    return {
        "message":"Welcome to Admin GameHome"
    }