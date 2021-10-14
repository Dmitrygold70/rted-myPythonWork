import sys
"""
Ask the user for distance in Feet, print it in Centimeters (1 Foot = 30.48 Centimeters)
"""
# coefficient feet to cm is 30.48
feet2Sm = 30.48

if __name__ == '__main__':
    # if the distance appears as a argument use it else ask to enter the distance
    if len(sys.argv) > 1:
        distance = float(sys.argv[1])
    else:
        distance = float(input("Please enter the distance in Feet: "))

    # Print conversion
    print(f"{distance} Feet equal to {distance * feet2Sm} Centimeters")
