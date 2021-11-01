from Day07_HW.Wheel import Wheel


class Vehicles(Wheel):

    def __init__(self, drivable=True, *args):
        # 2. Vehicles do not drive unless all wheels have equal radius values, no punctured wheels, and air percentage above 60%
        # 3. Member drivable will update according to calls vehicle methods add/del wheel and drive
        self.drivable = drivable
        self.wheels_list = []
        for arg in args:
            self.wheels_list.append(arg)
        super().__init__(radius=)

    def __str__(self):
        return f'drivable: {self.drivable}'

    def drive(self, distance):

        # 1. When a vehicle drives, air percentage lowers 1% per 1KM
        pass

    def add_wheel(self, wheel: Wheel):
        self.wheels_list.append(wheel)
        # TODO add verification for the wheels amount and its pressure


    def del_wheel(self, wheel: Wheel):
        self.wheels_list.remove(wheel)
        # TODO add verification for the wheels amount and its pressure
