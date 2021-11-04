class Point:
    def __init__(self, x=0, y=None):

        self.x = x

        if y is None:
            self.y = x
        else:
            self.y = y

    def show(self):
        print('({}, {})'.format(self.x, self.y))


if __name__ == '__main__':
    p1 = Point()
    p2 = Point(10,20)
    p3 = Point(5)
    p4 = Point(5, 0)
    p5 = Point("abc", "xyz")


    p1.show()
    p2.show()
    p3.show()
    p4.show()
    p5.show()

