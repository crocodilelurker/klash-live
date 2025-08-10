from fastapi import FastAPI
from app.configurations import connectDB
from contextlib import asynccontextmanager
from app.routes.UserRoutes import router as UserRouter
from app.routes.TournamentRoutes import router as TournamentRouter
from app.routes.GameRoutes import router as GameRouter

from app.routes.AdminRoutes.User import router as AdminUserRouter
from app.routes.AdminRoutes.Game import router as AdminGameRouter
from app.routes.AdminRoutes.Tournament import router as AdminTournamentRouter
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


app.include_router(AdminUserRouter)
app.include_router(AdminTournamentRouter)
app.include_router(AdminGameRouter) 


app.include_router(UserRouter)
app.include_router(TournamentRouter)
app.include_router(GameRouter)
