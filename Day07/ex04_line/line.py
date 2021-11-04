from point import Point


class Line:
    count = 0

    def __init__(self, x1, y1, x2, y2):
        self.point_a = Point(x1, y1)
        self.point_b = Point(x2, y2)
        Line.count += 1
        print("created Line", hex(id(self)))

    def __del__(self):
        Line.count -= 1
        print("deleted Line", hex(id(self)))

    def show(self):
        print("({}, {}) --> ({}, {})".format(
            self.point_a.x, self.point_a.y,
            self.point_b.x, self.point_b.y
        ))


if __name__ == '__main__':
    line1 = Line(10, 20, 30, 40)
    line1.show()
    line1.point_a.show()
    line1.point_b.show()
    #
    # del line1


