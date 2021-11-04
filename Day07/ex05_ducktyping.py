from ex03_point06 import Point
from ex04_line.line import Line


class Person:
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln

    def show(self):
        print("(fn: {}, ln: {})".format(self.first_name, self.last_name))


if __name__ == '__main__':
    items = [
        Point(10,20),
        Line(1,2,3,4),
        Person("Moshe","Levi"),
        Point(111,222)
    ]

    print("\n=======\n")

    for item in items:
        # print(item.show)
        item.show()

    print("\n=======\n")









