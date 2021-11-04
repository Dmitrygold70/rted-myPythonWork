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
        # new_point = Point()
        # new_point.x = self.x + other.x
        # new_point.y = self.y + other.y
        # return new_point
        return Point(self.x+other.x, self.y+other.y)



