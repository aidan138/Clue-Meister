from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime

class ClueType(str, Enum):
    BLOOD = "blood"
    FOOTPRINT = "footprint"
    CLOTHING = "clothing"
    AUDIO = "audio"
    NOTE = "note"
    SIGNAL = "signal"
    SIGHTING = "sighting"
    OTHER = "other" 

class Clue(BaseModel):
    class Location(BaseModel):
        longitude: float
        latitude: float
        desc: Optional[str] = None

    timestamp: datetime
    location: Location
    type: ClueType
    description: str
    source: str
    urgency: Optional[float] = None # To be computed