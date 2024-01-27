class Quest:
    def __init__(self, n, at, qt, p, rt, l = None):
        """
        Quests have a name, description, belong to different categories, have different point values, and for location-based quests, location
        Quest categories:
            Emote
            Wear brands
            Treasure Hunt
        """
        self.name = n
        self.description = None
        self.action_type = at
        self.quest_type = qt
        self.points = p
        self.refresh_time = rt
        self.location = l

        self.get_description()
    def get_description(self):
        """
        Description of quest category, should use data of self.name, self.action_type, self.quest_type, self.location if applicable
        """
        pass
