class Shekels:
    def __init__(self, shekels, agorot):
        self.shekels = shekels
        self.agorot = agorot

    def __repr__(self):
        return 'Shekels(shekels={}, agorot={}'.format(
            self.shekels, self.agorot
        )

    def __eq__(self, other):
        if isinstance(other, Shekels):
            return self.shekels == other.shekels and self.agorot == other.agorot
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Shekels):
            if self.shekels == other.shekels:
                return self.agorot < other.agorot
            else:
                return self.shekels < other.shekels
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, Shekels):
            return self < other or self == other
        else:
            return NotImplemented
