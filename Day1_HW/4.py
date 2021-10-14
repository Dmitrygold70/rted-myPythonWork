import sys
"""
Ask the user for two integers. print their sum, subtraction, division, multiplication, and
average (assume valid input).
"""


if __name__ == '__main__':
    # if the numbers appear as a arguments use them else ask to enter the numbers
    if len(sys.argv) == 3:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    else:
        print("Please enter the two integers")
        num1 = int(input("\tthe first number: "))
        num2 = int(input("\tthe second number: "))

    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("illegal operation, Can't divide to 0")

    print(f"{num1} * {num2} = {num1 * num2}")
    print(f"avg({num1}, {num2}) = {(num1 + num2) / 2}")
