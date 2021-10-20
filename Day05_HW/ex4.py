"""
Create a program that reads a file name from the user.
    assuming that files is a text file with one integer per line (encoding:UTF8, newline:LF) do the following:
        a) calculate and print the sum of the numbers
        b) read a name of another file name to create. create a binary file with that name
            that will contain the list (your choice of byte-size and byte-order)
        c) Create a program that reads files like the one you created in (b) and prints their sum.
"""
import os


if __name__ == '__main__':

    infile = input('Please enter the file name:\n>').strip()
    nums = list()
    if os.path.isfile(infile):
        with open(infile, 'r') as f:
            lines = f.readlines()
            nums = [int(num.strip()) for num in lines if len(num) > 0]

            print(f'The sum of the numbers imported from the text file is {sum(nums)}')

        bin_file = input('Please enter the name of the binary file o save the numbers list to:\n>')
        if os.path.normpath(bin_file):
            with open(bin_file, 'wb') as bf:
                for n in nums:
                    bf.write(n.to_bytes(4, byteorder='big'))

        with open(bin_file, 'rb') as bf:
            read_int = bf.read(4)
            nums.clear()
            while read_int:
                nums.append(int.from_bytes(read_int, "big"))
                read_int = bf.read(4)
            print(f'The sum of the numbers imported from the binary file is {sum(nums)}')

    else:
        print('The file does not exist')
