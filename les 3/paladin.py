from les2.character import Character

class Paladin(Character):

    def __init__(self, name, health, damage, defence, type = 'human'):
        Character.__init__(self, name, health, damage, defence, type)
    def take_damage(self, damage):
        damage -= self.defence
        Character.take_damage(self, damage)

    def atack(self, target):
        damage = self.damage
        if target.type == 'zom':
            damage *= 1.2
        target.take_damage(damage)

