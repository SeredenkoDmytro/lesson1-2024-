from les2.character import Character


class Berserk(Character):

    def __init__(self, name, health, damage, defence, type = 'human'):
        Character.__init__(self, name, health, damage, defence, type)
        self.max_health = health

    def count_additional_damage(self):
        return max(round(self.damage * (1 - self.health / self.max_health), 2), 0)

    def __str__(self):
        return Character.__str__(self) + f"\nДод. шкода {self.count_additional_damage()}"

    def atack(self, target):
        damage = self.damage + self.count_additional_damage()
        target.take_damage(damage)

