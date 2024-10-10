from les2.character import Character
from paladin import Paladin
from berserk import Berserk
from Samurai import Samurai


players_list = []
player1_name = input("Вандіть ім'я первого гравця")
player1_clаss = input("Внесіть класс ").lower()


if player1_clаss == "paladin":
    player1 = Paladin(player1_name, 100, 15, 0)
elif player1_clаss == "berserk":
    player1 = Berserk(player1_name, 100, 15, 0)
elif player1_clаss == "samurai":
    player1 = Samurai(player1_name, 100, 15, 0)
else:
    player1 = Character(player1_name, 100, 15, 0)


print(player1)
players_list.append(player1)



player2 = Samurai("Petya", 100, 5, 0)
player2.show_stats()

while player1.health > 0 and player2.health > 0:
    player1.atack(player2)
    player2.atack(player1)
    print(f"\n{player1}\n{player2}\n")

