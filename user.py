from player import Player


class User(Player):

    def ask(self):
        return input()