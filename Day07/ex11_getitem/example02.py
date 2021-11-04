class ByX:

    def __init__(self, mul):
        self.mul = mul

    def __getitem__(self, item):
        if item > 5:
            raise IndexError

        return item * self.mul


if __name__ == '__main__':
    b10 = ByX(10)

    for n in b10:
        print(n)
