class  Character:
    name = ""
    health = 100
    damage = 1
    defence = 0
    intelligence = 10
    agility = 10

    def __init__(self, name, health, damage, defence, intelligence, agility):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence
        self.intelligence = intelligence
        self.agility = agility
    def show_stats(self):
        print(f" -- {self.name}--\n   HP:{self.health}\n"
              f"   DMG:{self.damage}\n   DEF:{self.defence}\n"
              f"   INT:{self.intelligence}\n" f"   AG:{self.agility}")