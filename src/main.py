from clue_meister.agents.cm import ClueMeister


if __name__ == "__main__":
    cm = ClueMeister(name="Test-CM")
    print(cm.process_request("Hello Clue Master"))
