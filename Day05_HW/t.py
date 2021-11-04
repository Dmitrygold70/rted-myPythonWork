def summ():
    global a
    global b
    print(f'{a + b}')


def inp_a():
    global a
    a = int(input("Please enter the new value for A ").strip())


def inp_b():
    global b
    b = int(input("Please enter the new value for A ").strip())


a, b = 0, 0
menu = {'1': ['1) Set a new Value for A', inp_a()],
        '2': ['2) Set a new Value for B', inp_b()],
        '3': ['3) to get the sum A + B', summ()],
        'q': ['q) Quit ',]}


if __name__ == '__main__':

    while True:
        for k in menu:
            print(menu[k][0])

        choice = input('>').strip().lower()
        if choice not in menu.keys():
            print('incorrect choice')
            continue
        if choice == '1':
            a = int(input("Please enter the new value for A ").strip())
        elif choice == 'q':
            break

        menu[choice[1]()]


