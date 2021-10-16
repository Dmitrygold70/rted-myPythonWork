"""
Create an Menu program that handles two integer variables A & B. them menu will have
the following options:
a) Set a new Value for A - will input the user for a new value for A
b) Set a new Value for B - will input the user for a new value for B
c) Save to File - will save the values of the variables to a file (data.txt)
d) Load from File - will load the data of A & B from a text file
e) Quit - will quit the program
"""


def set_int(prompt: str):
    msg = (input(prompt).strip())
    if not msg.strip().isnumeric():
        print('incorrect input')
    else:
        return int(msg)


a, b = 0, 0
file = 'data.txt'
menu_d = {'a': 'a) Set a new Value for A',
          'b': 'b) Set a new Value for B',
          'c': 'c) Save to File',
          'd': 'd) Load from File',
          'p': 'p) Print A and B',
          'e': 'e) Quit'}

if __name__ == '__main__':
    while True:
        for el in menu_d:
            print(menu_d[el])
        choice = input('>').strip().lower()
        if choice not in menu_d:
            print('incorrect choice')
        elif choice == 'a':
            a = set_int("Please enter the new value for A ")

        elif choice == 'b':
            b = set_int("Please enter the new value for B ")

        elif choice.find('c') != -1:
            with open(file, 'w') as infile:
                infile.write(f'A = {a}\n')
                infile.write(f'B = {b}\n')

        elif choice.find('d') != -1:
            with open(file, 'r') as fromfile:
                lines = fromfile.readlines()
                for line in lines:
                    if line != '':
                        words = line.split('=')
                        if words[0].upper().find('A') != -1:
                            a = int(words[1].strip())
                        elif words[0].upper().find('B') != -1:
                            b = int(words[1].strip())

        elif choice.find('e') != -1:
            break
        elif choice == 'p':
            print(f'A = {a}; B = {b}')
