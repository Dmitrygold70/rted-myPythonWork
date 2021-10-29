import random


class Wheel:
    # 4. The wheel will be initialized with a random air percentage values between 85%-95%, unless specifically set.
    def __init__(self, radius, puncture=False, air_percentage=random.randrange(85, 95)):
        self.radius = radius
        self.puncture = puncture
        self.air_percentage = air_percentage

    def show(self):
        return f'R {self.radius}, air {self.air_percentage}%, isPuncture {self.puncture}'

    def in_flat(self, air_percentage):
        self.air_percentage = air_percentage

