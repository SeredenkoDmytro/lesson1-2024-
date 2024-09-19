import datetime


class  Character:
    name = ""
    birthday = 2010
    grop = 1
    ball = 8

    def __init__(self, name, birthday, grop, ball):
        self.name = name
        self.birthday = birthday
        self.grop = grop
        self.ball = ball

    def show_stats(self):
        print(f" -- {self.name}--\n   Год рождения:{self.birthday}\n"
              f"   Група:{self.grop}\n   Средний бал:{self.ball}\n")

    def age(self):
        current_year = datetime.date.today().year
        return current_year - self.birthday

    def show_age(self):
        print(f"Студенту {self.age()} лет" )

    def __str__(self):
        return f" -- {self.name}--\n   Год рождения:{self.birthday}\n" \
              f"   Група:{self.grop}\n   Средний бал:{self.ball}\n"
