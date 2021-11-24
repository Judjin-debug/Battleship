import random
import functools
from board import Board
from ship import Ship
from dot import Dot
from user import User
from ai import AI


class Game:

    def __init__(self, n=6, m=6, ship_sizes_tuple=(3, 2, 2, 1, 1, 1)):
        self.n = n
        self.m = m
        self.ship_sizes_tuple = ship_sizes_tuple
        self.user_board = self.random_board(n, m, ship_sizes_tuple, False)
        self.ai_board = self.random_board(n, m, ship_sizes_tuple, True)
        self.user = User(self.user_board, self.ai_board)
        self.ai = AI(self.ai_board, self.user_board)

    @staticmethod
    def random_board(n, m, ship_sizes_tuple, hid):
        orientations = ['horizontal', 'vertical']
        if any([not isinstance(n, int), not isinstance(m, int), n < 1, m < 1]):
            raise ValueError("Illegal dimension size")
        for item in ship_sizes_tuple:
            if any([not isinstance(item, int), item < 1]):
                raise ValueError("Illegal ship size")
            elif item > n and item > m:
                raise ValueError("Ship is too long for this field")
        if (n + 2) * (m + 2) < functools.reduce(lambda a, b: a + b, list(map(lambda a: a*2 + 2, ship_sizes_tuple))):
            raise ValueError("Impossible to place ships in such a small field")
        count_1 = 0
        while True:
            flag_2 = True
            new_board = Board(n, m, hid is True)
            for item in ship_sizes_tuple:
                count_2 = 0
                flag_1 = True
                while flag_1:
                    new_orientation = orientations[random.randrange(0, 2)]
                    if new_orientation == 'horizontal':
                        new_ship = Ship(item, Dot(random.randrange(0, n + 1 - item), random.randrange(0, m)), new_orientation)
                    elif new_orientation == 'vertical':
                        new_ship = Ship(item, Dot(random.randrange(0, n), random.randrange(0, m + 1 - item)), new_orientation)
                    else:
                        raise ValueError("Ship init failure")
                    try:
                        new_board.add_ship(new_ship)
                    except ValueError as e:
                        count_2 += 1
                        if count_2 > 5000:
                            flag_2 = False
                            break
                    else:
                        flag_1 = False
            count_1 += 1
            if count_1 > 100000:
                raise RuntimeError("Something went wrong during generation")
            if flag_2 is True:
                return new_board

    @staticmethod
    def greet():
        print("Welcome to the game of Battleship")
        print("Enter the coordinates separated by a whitespace (e.g. '1 2', row-column)")

    def loop(self):
        score = [0, 0]
        while True:
            game = 1
            print("Starting a new game")
            print(f"Game {game}")
            print("Displaying your board")
            self.user_board.print()
            print("Displaying enemy's board")
            self.ai_board.print()
            turn = 1
            while True:
                print(f"Turn {turn}")
                print("Now enter the coordinates: ")
                self.user.move()
                print("Displaying enemy's board")
                self.ai_board.print()
                print("Now is AI's turn")
                self.ai.move()
                print("Displaying your board")
                self.user_board.print()
                user_hp = self.user_board.hp_check
                ai_hp = self.ai_board.hp_check
                if user_hp == 0 and ai_hp == 0:
                    print("The game ended in a draw")
                    print(f"The score is now Player: {score[0]}, AI: {score[1]}")
                    break
                elif ai_hp == 0:
                    print("You've won the game")
                    score[0] += 1
                    print(f"The score is now Player: {score[0]}, AI: {score[1]}")
                    break
                elif user_hp == 0:
                    print("You've lost the game")
                    score[1] += 1
                    print(f"The score is now Player: {score[0]}, AI: {score[1]}")
                    break
                turn += 1
            check = input("One more game?[y/N]")
            if check.lower() == 'y':
                game += 1
                self.user_board = self.random_board(self.n, self.m, self.ship_sizes_tuple, False)
                self.ai_board = self.random_board(self.n, self.m, self.ship_sizes_tuple, True)
                self.user = User(self.user_board, self.ai_board)
                self.ai = AI(self.ai_board, self.user_board)
            else:
                break

    def start(self):
        self.greet()
        self.loop()
