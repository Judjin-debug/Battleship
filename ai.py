from player import Player
import random
from dot import Dot


class AI(Player):

    def ask(self):
        return str(random.randrange(1, self.enemy_board.get_n + 1)) + " " + str(random.randrange(1, self.enemy_board.get_m + 1))

    def move(self):
        flag = True
        while flag:
            try:
                answer = self.ask()
                if not self.input_check(answer):
                    raise ValueError("Illegal input")
                processed_answer = self.input_processing(answer)
                self.enemy_board.shot(Dot(int(processed_answer[0]) - 1, int(processed_answer[1]) - 1))
            except ValueError as e:
                pass
            else:
                print(f"Shot coordinate is {int(processed_answer[0])}, {int(processed_answer[1])}")
                flag = False