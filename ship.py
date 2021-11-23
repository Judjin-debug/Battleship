from dot import Dot


class Ship:

    def __init__(self, length, head, orientation):
        if not isinstance(length, int) or length < 0:
            raise ValueError("Ship length must be a non-negative integer")
        elif orientation not in ['horizontal', 'vertical']:
            raise ValueError("No such ship orientation exists. It must be either vertical or horizontal")
        else:
            self.length = length
            self.head = head
            self.orientation = orientation
            self.lives = length

    @property
    def dots(self):

        result = [self.head]
        if self.orientation == 'horizontal':
            for i in range(1, self.length):
                result.append(Dot(self.head.get_x() + i, self.head.get_y()))
        else:
            for i in range(1, self.length):
                result.append(Dot(self.head.get_x(), self.head.get_y() + i))
        return result

    @staticmethod
    def init_info():
        print("The ship head will point either upwards or left, meaning that the extra sections get"
              "appended to the right or down")