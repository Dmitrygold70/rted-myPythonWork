"""
Write a program that reads a positive integer from the user, if the input is not a positive
integer, write an error message and read again until a valid input is given
"""

if __name__ == '__main__':
    num = -1
    while num < 0:
        num = int(input("Please enter an integer: "))
