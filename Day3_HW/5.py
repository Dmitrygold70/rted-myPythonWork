"""
    a) Create a program that read width and height from the user and prints a rectangle
    of that dimension (on the terminal using '*' characters)
    b) Do the same but make the rectangle hollow (the inside of the rectangle is made
    of space characters)
"""

width = int(input("Please enter the width: "))
height = int(input("Please enter the height: "))
# a)
for h in range(height):
    for w in range(width):
        print('*', end='')
    print()

# b)
for h in range(height):
    for w in range(width):
        if h == 0 or h == height - 1 or w == 0 or w == width - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
