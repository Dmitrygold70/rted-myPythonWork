class Person:
    def __init__(self, name, last_name, pid):
        self.name = name
        self.last_name = last_name
        self.pid = pid

    def show(self):
        return f'{self.name:10s}{self.last_name:10s}{self.pid:09d}'

    def set_name(self, name):
        self.name = name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_id(self, pid):
        self.pid = pid


if __name__ == '__main__':
    persons = list()
    persons.append(Person('Moshe', 'Dayan', 1))
    persons.append(Person('Yossi', 'Perez', 2))
    persons.append(Person('Villy', 'Crep', 3))

    for p in persons:
        print(p.show())
