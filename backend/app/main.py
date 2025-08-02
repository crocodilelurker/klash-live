from fastapi import FastAPI
from app.configurations import connectDB
from contextlib import asynccontextmanager
from app.routes.UserRoutes import router as UserRouter
@asynccontextmanager
async def lifespan(app: FastAPI):
    connectDB()
    yield
    print("Shutting down the application...")
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {
        "message":"Welcome to home"
    }
app.include_router(UserRouter)