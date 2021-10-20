"""
Make the program in the question above read the number range and number of guesses
from a file
"""

"""
Make the program in the question above read the number range and number of guesses
from a file.
"""
nums = list()
number_file = 'c:\\bugs\\in_nums.bin'


def file_read(file):
    global nums
    with open(file, 'rb') as bf:
        next_int = bf.read(4)
        while next_int:
            nums.append(int.from_bytes(next_int, 'big'))
            next_int = bf.read(4)


file_read(number_file)
print(nums)
