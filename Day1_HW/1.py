import sys


if __name__ == '__main__':
    # if the name appears as a argument use it else ask to enter the name
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = input("Please enter your name: ")

    # a print your name: David
    print(name)

    # b print your name decorated with asterisks using print statements:
    print('*' * (len(name) + 4))
    print('*', name, '*')
    print('*' * (len(name) + 4))
    # c try to do the same but using only a single print statement using a multi-line string
    print('*' * (len(name) + 4) + '\n*', name, '*\n' + '*' * (len(name) + 4))

    # d try to do the same but using a single parentheses string
    print(f"{'*' * (len(name) + 4)}\n* {name} *\n{'*' * (len(name) + 4)}")
