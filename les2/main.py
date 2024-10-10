from character import Character


player1 = Character("Vasya", 300, 20, 0)
player1.show_stats()


player2 = Character("Petya", 150, 12, 0)
player2.show_stats()






def battle(character1, character2):
    while character1.is_alive() and character2.is_alive():
        print(f"\n{character1.name} ударил {character2.name}")
        character2.take_damage(character1.damage)

        if not character2.is_alive():
            print(f"{character2.name} умер. {character1.name} выиграл!")
            break

        print(f"\n{character2.name} ударил {character1.name}")
        character1.take_damage(character2.damage)

        if not character1.is_alive():
            print(f"{character1.name} умер. {character2.name} выиграл!")
            break

battle(player1, player2)