import random
from person import Person
from work import Work
from rest import Rest
from action import Action
from exceptions import DeathError, DepressionError, BankruptcyError


people = [
    Person(name="Тарас", health=90, mood=100, money=70),
    Person(name="Марія", health=90, mood=70, money=50),
    Person(name="Петро", health=80, mood=60, money=40),
    Person(name="Андрiй", health=100, mood=40, money=60),
    Person(name="Дмитро", health=70, mood=120, money=35)
]


actions = [
    Work(name="Піти на роботу"),
    Rest(name="Сходити в парк"),
    Action(name="Піти в лікарню", health=30, mood=-10, money=-30)
]


def print_all_people(people):
    print("\nСтан усіх людей:")
    for person in people:
        print(person)
    print("\n")



while people:
    for person in people[:]:
        action = random.choice(actions)
        try:
            person.do(action)
        except (DeathError, DepressionError, BankruptcyError) as e:
            print(f"\n{e}")
            people.remove(person)
    print_all_people(people)
    if not people:
        print("Усі люди вибули.")
        break
