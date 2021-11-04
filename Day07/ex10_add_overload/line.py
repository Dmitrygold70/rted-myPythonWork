from point import Point

class Line:

    def __init__(self, x1, y1, x2, y2):
        self.point_a = Point(x1, y1)
        self.point_b = Point(x2, y2)

    def __str__(self):
        return "({}, {}) --> ({}, {})".format(
            self.point_a.x, self.point_a.y,
            self.point_b.x, self.point_b.y
        )

    def __repr__(self):
        return "Line(x1={}, y1={}, x2={}, y2={})".format(
            self.point_a.x, self.point_a.y,
            self.point_b.x, self.point_b.y
        )


if __name__ == '__main__':
    line1 = Line(10, 20, 30, 40)
    line1.show()
    line1.point_a.show()
    line1.point_b.show()
    #
    # del line1


