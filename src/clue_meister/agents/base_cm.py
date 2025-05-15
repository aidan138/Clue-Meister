from autogen import AssistantAgent
import autogen
from abc import ABC, abstractmethod
from src.clue_meister.knowledge.clue_set import KnowledgeBase


class BaseAgent(AssistantAgent):
    def __init__(
            self,
            name,
            system_message,
            is_termination_msg = None,
            max_consecutive_auto_reply = None,
            human_input_mode = "NEVER",
            description = None, 
            ClueSet: KnowledgeBase | None  =  None
            ):
        super().__init__(name,
                        system_message,
                        llm_config={
                        #     "config_list": autogen.config_list_from_json( # Load the Open AI configuration hidden json
                            #     "OAI_CONFIG_LIST",
                            #     file_location="../config",
                            #     filter_dict={
                            #         "model": {
                            #             "gpt-4o-mini",
                            #             "gpt-3.5-turbo",
                            #         }
                            #     }
                        # ),
                        "model": "llama3",
                        "base_url": "http://localhost:11434/v1",  # Ollama default base
                        "api_key": "ollama",  # Doesn't matter; just a placeholder
                        "seed" : 13,
                        "temperature" : 0.8,
                        "top_p": 0.9
                        },
                        is_termination_msg=is_termination_msg,
                        max_consecutive_auto_reply=max_consecutive_auto_reply,
                        human_input_mode=human_input_mode,
                        description=description)
        #self.name = name
        self.mission_status = "process clues"
        self.ClueSet = KnowledgeBase

    
    
    
    def process_request(self, message):
        """Process incoming requests - must be implemented by specific agents"""
        return self.generate_reply([{"role": "user", "content": message}])

    def update_status(self, status):
        """Update agent's mission status"""
        self.mission_status = status
        return {"status": "updated", "new_status": status}

    def get_status(self):
        """Return current status"""
        return self.mission_status

if __name__ == "__main__":
    cm = BaseAgent(name="Clue", system_message="You are an expert detective trying to aid search and rescue efforts. You are trying to locate the victim and every second is vital. You are not trying to find a criminal you are trying to save a lost civilians life")
    response = cm.process_request("Respond with your best prediction of where the suspect is headed. Blood was found by a creak")
    print("ClueMeister:", response)