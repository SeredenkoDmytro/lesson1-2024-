from exceptions import DeathError, DepressionError, BankruptcyError
from action import Action
from work import Work
from rest import Rest

class Person:
    def __init__(self, name, health=100, mood=100, money=0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
        return f"=== {self.name} ===\nЗдоров'я: {self.health}\nНастрій: {self.mood}\nКапітал: {self.money}"

    def change_state(self, health=0, mood=0, money=0):
        self.health += health
        if self.health < 0:
            raise DeathError(f"{self.name} помер через обезсилення!")


        self.mood += mood
        if self.mood < 0:
            raise DepressionError(f"{self.name} впав у депресію!")

        self.money += money
        if self.money < 0:
            raise BankruptcyError(f"{self.name} обiднiв!")

    def do(self, action):
        if type(action) == Action:
            self.change_state(health=action.health, mood=action.mood, money=action.money)
        elif type(action) == Work:
            extra_money = action.money
            if self.mood > 90:
                extra_money *= 1.1
            self.change_state(health=action.health, mood=action.mood, money=extra_money)
        elif type(action) == Rest:
            extra_mood = action.mood
            if self.health < 40:
                extra_mood *= 0.8
            self.change_state(health=action.health, mood=extra_mood, money=action.money)
