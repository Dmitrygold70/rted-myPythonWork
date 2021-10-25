# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# with open('test.txt', 'w') as f:
#     f.write('line 1\n')

# with open('test.txt', 'wb') as f:
#     # lines  = f.readlines()
#     f.write(bytearray('line 2\n', 'utf8'))
#     f.write(int(1000).to_bytes(4, 'big'))
#
try:
    f = open('fiel','wr')
except Exception as e:
    print()