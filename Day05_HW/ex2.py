"""
Change the program in question 2 in the following ways:
a) make the file binary instead of txt (data.txt--> data.bin)
b) when the program starts, it load the file if it exists
c) add exceptions later (after we learn about them in the next lessons)
"""
import os

from Day05_HW import ex1


def get_from_file(infile):
    with open(infile, 'rb') as fromfile:
        n1 = int.from_bytes(fromfile.read(4), 'big')
        n2 = int.from_bytes(fromfile.read(4), 'big')
    return n1, n2


infile = 'data.bin'

if __name__ == '__main__':
    if os.path.exists(infile) and os.path.isfile(infile):
        a, b = get_from_file(infile)
    else:
        print('The data file did not found please initialize the A and B')
        a, b = 0, 0
    while True:
        for el in ex1.menu_d:
            print(ex1.menu_d[el])
        choice = input('>').strip().lower()
        if choice not in ex1.menu_d:
            print('incorrect choice')
        elif choice == 'a':
            a = ex1.set_int("Please enter the new value for A ")

        elif choice == 'b':
            b = ex1.set_int("Please enter the new value for B ")

        elif choice == 'c':
            with open(infile, 'wb') as infile:
                infile.write(a.to_bytes(4, byteorder='big'))
                infile.write(b.to_bytes(4, byteorder='big'))

        elif choice == 'd':
            get_from_file(infile)

        elif choice == 'e':
            break
        elif choice == 'p':
            print(f'A = {a}; B = {b}')
