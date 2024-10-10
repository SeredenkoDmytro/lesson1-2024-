from les2.character import Character

class Samurai(Character):
    def __init__(self, name, health, damage, defence, type='samurai'):
        super().__init__(name, health, damage, defence, type)
        self.hitmult = 1.0
        self.hits = 0

    def atack(self, target):
        damage = self.damage * self.hitmult
        target.take_damage(damage)

        if self.hits < 5:
            self.hitmult += 0.1
            self.hits += 1
        else:
            self.hitmult = 1.0
            self.hits = 0