class Person:

    def __init__(self, age):
        if not isinstance(age, int):
            raise TypeError("...int...")

        if not (0 <= age <= 120):
            raise ValueError("1...120")

        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, value):
        if not isinstance(value, int):
            raise TypeError("...int...")

        if not (0 <= value <= 120):
            raise ValueError("1...120")

        self._age = value


if __name__ == '__main__':
    p1 = Person(50)
    print(p1.get_age())
    # p1.set_age(300)
    p1._age = 300
    print(p1.get_age())



