class Character:
    name = ''
    health = 100
    damage = 1
    defence = 0
    type = 'human'

    def __init__(self, name, health, damage, defence, type):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence
        self.type = type

    def show_stats(self):
        print(f"-- {self.name} --\nЗдоров'я: {self.health}\n"
              f"Шкода: {self.damage}\nЗахист: {self.defence}\n"
              f"Тип: {self.type}")

    def __str__(self):
        return f"-- {self.name} --\nЗдоров'я: {self.health}\n" \
              f"Шкода: {self.damage}\nЗахист: {self.defence}"

    def take_damage(self, damage):
        #self.health -= damage
        #if self.health <= 0:
            #self.health = 0
            #print(f"{self.name} убит")
        #else:
            #print(f"{self.name} получает {damage} dmg. Сейчас у него: {self.health} здоровья")
        self.health = max(self.health - damage, 0)

    def is_alive(self):
        return self.health > 0

    def atack(self, target):
        target.take_damage(self.damage)
