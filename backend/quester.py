import json
from utils.quest import Quest
import random

class Quester:
    def __init__(self):
        self.filename = "quest_data.json"
        self.quest_limits = {"daily": 5, "weekly": 3, "challenge": 3}

    def generate_quests(self, quest_type):
        """
        Generate quests based on quest_type
        """
        quests = []
        with open(self.filename, 'r') as file:
            quest_data = json.load(file)
            for q in quest_data:
                if q["quest_type"] == quest_type:
                    quests.append(q)
    
        random.randint(0, 5)
        return quests
