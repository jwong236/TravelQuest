class Quest:
    def __init__(self, quest_data):
        """
        Initialize the Quest instance using a dictionary.
        Quests have a name, description, belong to different categories, have different point values, and for location-based quests, location
        Quest categories:
            Emote
            Wear brands
            Treasure Hunt

        :param quest_data: A dictionary containing keys 'name', 'description', 'quest_type', and 'points'.
        """
        self.name = quest_data.get('name')
        self.description = quest_data.get('description')
        self.quest_type = quest_data.get('quest_type')
        self.points = quest_data.get('points')