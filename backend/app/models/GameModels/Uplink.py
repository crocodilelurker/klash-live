from pydantic import BaseModel



class GameUplink(BaseModel):
    name: str
    description: str
    official_website: str
    cover_image_url: str
    match_format: str
