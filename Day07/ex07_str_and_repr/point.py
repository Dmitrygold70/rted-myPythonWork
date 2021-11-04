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

