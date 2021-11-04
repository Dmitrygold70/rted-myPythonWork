class Point:
    def __init__(self, x=0, y=None):
        if type(x) is not int:
            raise TypeError("x must be an int")

        if y is not None and type(y) is not int:
            raise TypeError("y must be an int")

        self.x = x

        if y is None:
            self.y = x
        else:
            self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return 'Point(x={}, y={})'.format(self.x, self.y)

    # self + other
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x+other.x, self.y+other.y)
        elif isinstance(other, int):
            return Point(self.x + other, self.y + other)
        else:
            return NotImplemented

    # other + self
    def __radd__(self, other):
        return self + other

    # self += other
    def __iadd__(self, other):
        if isinstance(other, Point):
            self.x += other.x
            self.y += other.y
        elif isinstance(other, int):
            self.x += other
            self.y += other
        else:
            return NotImplemented

        return self
