from models.clue_models import Clue
from datetime import datetime
from geopy.distance import geodesic

def compute_urgency(clue: Clue, current_time: datetime, current_location: tuple):
    """
    Computes a basic priority score for clues between distance and time elapsed.
    Uses both time and space considerations with an emphasis on the time.
    """
    clue_dist = geodesic((clue.location.latitude, clue.location.longitude), current_location).mi
    time_elapsed = (current_time - clue.timestamp).total_seconds() / 3600 # Get the time in hours
    clue.urgency = 0.6 * time_elapsed + 0.4 * clue_dist # TODO optimize units/ ratios later
    return clue.urgency

def sort_clues_by_priority(clues: list[Clues], current_time: datetime, current_location: tuple):
    return sorted(clues, key=lambda c : compute_urgency(c, current_time, current_location))
    
    
