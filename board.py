from dot import Dot
import functools


class Board:

    def __init__(self, size_x, size_y, hid):
        self.n = size_x
        self.m = size_y
        self.hid = hid
        self.field = [["O" for i in range(size_x)] for j in range(size_y)]
        self.quantity = 0
        self.ships = []

    def out(self, dot):
        return not all([dot.get_x() >= 0, dot.get_x() < self.n,
                        dot.get_y() >= 0, dot.get_y() < self.m])

    def add_ship(self, ship):
        if any(list(map(lambda ship_dot: self.out(ship_dot), ship.dots))):
            raise ValueError("Ship is out of bounds")
        elif any(list(map(lambda ship_dot: self.field[ship_dot.get_x()][ship_dot.get_y()] == 'B' or self.field[ship_dot.get_x()][ship_dot.get_y()] == '■', ship.dots))):
            raise ValueError("Impossible to place a ship because it encroaches already occupied space")
        else:
            self.ships.append(ship)
            self.quantity += 1
            for dot in ship.dots:
                self.field[dot.get_x()][dot.get_y()] = "■"
            self.contour(ship)

    def contour(self, ship):
        if ship.orientation == 'horizontal':
            for i in range(ship.length + 2):
                for j in range(3):
                    if not self.out(Dot(ship.dots[0].get_x() + i - 1, ship.dots[0].get_y() + j - 1)):
                        if self.field[ship.dots[0].get_x() + i - 1][ship.dots[0].get_y() + j - 1] != '■':
                            self.field[ship.dots[0].get_x() + i - 1][ship.dots[0].get_y() + j - 1] = 'B'
        if ship.orientation == 'vertical':
            for i in range(3):
                for j in range(ship.length + 2):
                    if not self.out(Dot(ship.dots[0].get_x() + i - 1, ship.dots[0].get_y() + j - 1)):
                        if self.field[ship.dots[0].get_x() + i - 1][ship.dots[0].get_y() + j - 1] != '■':
                            self.field[ship.dots[0].get_x() + i - 1][ship.dots[0].get_y() + j - 1] = 'B'

    def shot(self, dot):
        if self.out(dot):
            raise ValueError("Shot coordinate is out of bounds")
        else:
            if self.field[dot.get_x()][dot.get_y()] == 'X' or self.field[dot.get_x()][dot.get_y()] == 'T':
                raise ValueError("You can't repeat shot the same coordinate")
            elif self.field[dot.get_x()][dot.get_y()] in ['B', 'O']:
                self.field[dot.get_x()][dot.get_y()] = 'T'
                print("Miss")
            elif self.field[dot.get_x()][dot.get_y()] == '■':
                for ship in self.ships:
                    for ship_dot in ship.dots:
                        if ship_dot == Dot(dot.get_x(), dot.get_y()):
                            ship.lives -= 1
                self.field[dot.get_x()][dot.get_y()] = 'X'
                print("Hit")

    def print(self):
        print("     ", end="")
        for j in range(len(self.field[0])):
            print(str(j + 1) + " | ", end="")
        print("\n")
        if not self.hid:
            for i in range(len(self.field)):
                print(f" {i+1} | ", end="")
                for j in range(len(self.field[0])):
                    if self.field[i][j] == 'B':
                        print("O   ", end="")
                    else:
                        print(self.field[i][j] + "   ", end="")
                print("\n")
            print("\n")
        else:
            for i in range(len(self.field)):
                print(f" {i + 1} | ", end="")
                for j in range(len(self.field[0])):
                    if self.field[i][j] == 'X' or self.field[i][j] == 'T':
                        print(self.field[i][j] + "   ", end="")
                    else:
                        print('*   ', end="")
                print("\n")
            print("\n")

    def clear(self):
        self.field = [["O" for i in range(self.n)] for j in range(self.m)]
        self.quantity = 0
        self.ships = []

    @property
    def hp_check(self):
        return functools.reduce(lambda a, b: a + b, list(map(lambda a: a.lives, self.ships)))

    @property
    def get_n(self):
        return self.n

    @property
    def get_m(self):
        return self.m