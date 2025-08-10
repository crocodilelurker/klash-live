from fastapi import APIRouter
from app.models.GameModels.Uplink import GameUplink
from app.configurations import GameCollection
router= APIRouter(prefix="/gameAdmin",tags=["Admin Game"])

@router.get("/")
async def root():
    return {
        "message":"Welcome to Admin GameHome"
    }

from bson import ObjectId

@router.post("/create-game")
async def newGame(Game: GameUplink):
    game_dict = Game.model_dump()
    result = await GameCollection.insert_one(game_dict)

    # Add the stringified _id into the response object if needed
    game_dict["_id"] = str(result.inserted_id)

    return {
        "message": "Game created successfully",
        "game": game_dict
    }
