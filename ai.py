from player import Player
import random
from dot import Dot


class AI(Player):

    def ask(self):
        return [random.randrange(1, self.enemy_board.get_n + 1), random.randrange(1, self.enemy_board.get_m + 1)]

    def move(self):
        flag = True
        while flag:
            try:
                processed_answer = self.ask()
                self.enemy_board.shot(Dot(processed_answer[0] - 1, processed_answer[1] - 1))
            except ValueError as e:
                pass
            else:
                print(f"Shot coordinate is {processed_answer[0]}, {processed_answer[1]}")
                flag = False
