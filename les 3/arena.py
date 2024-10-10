from les2.character import Character
from paladin import Paladin
from berserk import Berserk
from Samurai import Samurai

players_list = []


class Arena:

    players =[]
    def __init__(self, players = ()):
        for player in players:
            self.players.append(player)


    def add_player(self):
        player_name = input("Введіть ім'я первого гравця")
        player_hp = input("Введіть здоров'я гравця")
        player_dmg = input("Введіть шкоди гравця")
        player_def = input("Введіть захист гравця")
        player_clаss = input("Введіть класс ").lower()

        if player_clаss == "paladin":
            player1 = Paladin(player_name, player_hp, player_dmg, player_def,player_clаss)
        elif player_clаss == "berserk":
            player1 = Berserk(player_name, player_hp, player_dmg, player_def,player_clаss)
        elif player_clаss == "samurai":
            player1 = Samurai(player_name, player_hp, player_dmg, player_def,player_clаss)
        else:
            player1 = Character(player_name, player_hp, player_dmg, player_def,player_clаss)


