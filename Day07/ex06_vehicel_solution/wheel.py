from random import randint


class Wheel:
    #def __init__(self, puncture, radius, air=randint(85, 95)):
    def __init__(self, puncture, radius, air=None):
        self.puncture = puncture
        self.radius = radius

        if air is not None:
            self.air = air
        else:
            self.air = randint(85, 95)

    def show(self):
        print("Wheel(puncture={}, radius={}, air={})".format(
            self.puncture, self.radius, self.air
        ))


    # TODO: inflate method

if __name__ == '__main__':
    w1 = Wheel(True, 50)
    w2 = Wheel(False, 40)
    w3 = Wheel(True, 35)

    w1.show()
    w2.show()
    w3.show()

    print("\n=======\n")

    wheels = [w1, w2, w3]

    for wheel in wheels:
        wheel.show()

    wheels.append(Wheel(False, 20))
