class Point:
    count = 0

    def __init__(self, x=0, y=None):
        if type(x) is not int:
            raise TypeError("x must be an int")

        if y is not None and type(y) is not int:
            raise TypeError("y must be an int")

        Point.count += 1

        self.x = x

        if y is None:
            self.y = x
        else:
            self.y = y

        print("created Point {}, total: {}".format(hex(id(self)), Point.count))

    def show(self):
        print('({}, {})'.format(self.x, self.y))

    def __del__(self):
        Point.count -= 1
        print("deleted Point {}, total: {}".format(hex(id(self)), Point.count))




if __name__ == '__main__':
    p1 = Point()
    p2 = Point(10,20)
    p3 = Point(5)
    p4 = Point(5, 0)
    #p5 = Point("abc", "xyz")


    p1.show()
    p2.show()
    p3.show()
    p4.show()
    #p5.show()

