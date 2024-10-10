from action import Action

class Work(Action):
    def __init__(self, name, health=-10, mood=-15, money=30):
        super().__init__(name, health, mood, money)
