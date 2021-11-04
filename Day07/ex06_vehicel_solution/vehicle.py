from wheel import Wheel

class Vehicle:

    # def __init__(self, wheels=[]):
    #     self.wheels = wheels

    def __init__(self, wheels=None):
        if wheels is not None:
            self.wheels = wheels
        else:
            self.wheels = []


if __name__ == '__main__':

    v1 = Vehicle()
    v2 = Vehicle()

    v1.wheels.append(Wheel(False, 30, 90))
    v1.wheels.append(Wheel(False, 30, 80))
    v1.wheels.append(Wheel(False, 30, 70))
    v1.wheels.append(Wheel(False, 30, 75))

    print("v1 wheels:")
    for w in v1.wheels:
        w.show()
    print()

    print("v2 wheels:")
    for w in v2.wheels:
        w.show()
    print()

