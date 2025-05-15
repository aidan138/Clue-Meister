from base_cm import BaseAgent
from typing import Dict, List, Tuple, Optional
from datetime import datetime
import json


CLUE_MEISTER_ROLE = f"""You are an expert at analyzing search and rescue clues to save lives. 
Your role is to:
1. Sort clues by criteria
2. Prioritize clues
3. Identify patterns in sets of clues
4. Initiate further inquires
"""

class ClueMeister(BaseAgent):
    def __init__(self, name: str):
        super().__init__(name=name,
                         system_message=CLUE_MEISTER_ROLE)
    

if __name__ == "__main__":
    cm = ClueMeister("Test-CM")
    response = cm.process_request("We found blood on the north side creak.")
    print(response)
