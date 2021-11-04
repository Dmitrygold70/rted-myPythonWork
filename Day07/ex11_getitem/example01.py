class ByX:

    def __init__(self, mul):
        self.mul = mul

    def __getitem__(self, item):
        return item * self.mul


if __name__ == '__main__':
    b10 = ByX(10)

    print(b10[0])
    print(b10[1])
    print(b10[2])
    print(b10[3])
