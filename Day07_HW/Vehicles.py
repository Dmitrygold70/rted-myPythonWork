from Day07_HW.Wheel import Wheel


class Vehicles(Wheel):

    def __init__(self, drivable=True, *args):
        # 2. Vehicles do not drive unless all wheels have equal radius values, no punctured wheels, and air percentage above 60%
        # 3. Member drivable will update according to calls vehicle methods add/del wheel and drive
        self.drivable = drivable
        self.wheels_list = [args]
        super().__init__()

    def show(self):
        return f'drivable: {self.drivable}'

    def drive(self):
        # 1. When a vehicle drives, air percentage lowers 1% per 1KM
        pass

    def add_del_wheel(self, wheel):
        pass
