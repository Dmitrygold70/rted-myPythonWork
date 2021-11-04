"""
2)
    a) Create a list of words (e.g. fruits). ask the user for a string input and then tell
    them if it's in the list or not.
    b) Do the same as the question above but replace the list with a dictionary (key =
    first character of the fruit).
"""
fruits = ['apple', 'orange', 'peach', 'apricot']
fruits_dict = {'a': 'apple', 'o': 'orange', 'p': 'peach'}

if __name__ == '__main__':
    inp = input("Please enter a string: ")
    # a)
    if inp not in fruits:
        print("The {inp} is not in the fruits list.")

    # b)
    if inp not in fruits_dict.values():
        print("The {inp} is not in the fruits dictionary.")
