from action import Action

class Rest(Action):
    def __init__(self, name, health=10, mood=5, money=-20):
        super().__init__(name, health, mood, money)
