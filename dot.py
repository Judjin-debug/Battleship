class Dot:

    def __init__(self, x, y):
        if any([not isinstance(x, int), not isinstance(y, int)]):
            raise ValueError("Class Dot object instance should be initialized with integers")
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y