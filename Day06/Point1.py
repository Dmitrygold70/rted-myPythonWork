class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        return f'({self.x}, {self.y})'

    def __del__(self):
        pass
