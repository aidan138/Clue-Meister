from pydantic import BaseModel

class Clue(BaseModel):
    class Location(BaseModel):
        coordinates: list[float]
        desc: str
    time: str
    location: Location
    type: str
    details: str
    source: str