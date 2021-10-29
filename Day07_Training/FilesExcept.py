text = "Hello World"

try:
    with open("file.txt", 'w') as f:
        f.write(text + "\n")
except PermissionError:
    print("File permissions error")

try:
    with open("file1_text.bin", 'wb') as bf:
        bf.write(bytearray(text, 'utf8'))
except PermissionError:
    print("File permissions error")

a = int(input('Enter the number\n>'))
b = int(input('Enter the number\n>'))

try:
    with open('file1_num.bin', 'wb') as bf:
        bf.write(a.to_bytes(4, 'big'))
        bf.write(b.to_bytes(4, 'big'))

except PermissionError:
    print("File permissions error")

try:
    with open('file2_num.bin', 'wb') as bf:
        bf.write(a.to_bytes(4, 'little'))
        bf.write(b.to_bytes(4, 'little'))
except PermissionError:
    print("File permissions error")

try:
    with open('file1_num.bin', 'rb') as bf:
        a = int.from_bytes(bf.read(4), 'big')
        b = int.from_bytes(bf.read(4), 'big')
except PermissionError:
    print("File permissions error")
