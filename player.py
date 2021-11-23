import re
from dot import Dot


class Player:

    def __init__(self, own_board, enemy_board):
        self.own_board = own_board
        self.enemy_board = enemy_board

    def ask(self):
        pass

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
                print("Wrong input, please try again")
            else:
                print(f"Shot coordinate is {int(processed_answer[0])}, {int(processed_answer[1])}")
                flag = False

    @staticmethod
    def input_check(input_text):

        if not re.search("[0-9]+\s+[0-9]+", input_text):
            return False
        return True

    @staticmethod
    def input_processing(input_text):
        return re.findall("\d+", input_text)
