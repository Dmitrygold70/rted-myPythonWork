import sys
"""
 Ask the user for their name and age, print both in the same sentence:
Your name is ____ and you are ____ years old
"""

if __name__ == '__main__':
    # if parameters supplied as a command line arguments use them, else ask to enter
    if len(sys.argv) == 3:
        name = sys.argv[1]
        age = int(sys.argv[2])
    else:
        name = input("Please enter your name: ")
        age = int(input("Please enter your age: "))

    print(f"Your name is {name} and you are {age} years old")
