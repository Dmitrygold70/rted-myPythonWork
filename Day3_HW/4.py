"""
    Read a list of positive integers from the user until an invalid input is given. add the
    numbers to a list, and then:
"""
numbers = list()
while True:
    inp = input("Please enter the positive integer: ")
    if inp.isnumeric() and int(inp) >= 0:
        numbers.append(int(inp))
    else:
        break
# a) print the list in a single line
print()
print('a) ', end='')
for n in numbers:
    print(n, '', end='')
print()

# b) print the list's sum
# s = 0
# for n in numbers:
#     s += n
# print(s)
print('b)', sum(numbers))

# c) print the maximum value
if len(numbers) > 0:
    m = numbers[0]
else:
    m = 0
for n in numbers:
    if n > m:
        m = n
# print(m)
print('c)', max(numbers))

# d) print only the even numbers in a single line
print('d) ', end='')
for n in numbers:
    if n % 2 == 0:
        print(n, '', end='')
# e) print only the odd numbers in a single line
print('\ne) ', end='')
for n in numbers:
    if n % 2 != 0:
        print(n, '', end='')
# f) print whether there are more even or odd numbers.
print('\nf) ', end='')
odd = list()
even = list()
for n in numbers:
    if n % 2 != 0:
       odd.append(n)
    else:
        even.append(n)
if len(even) > len(odd):
    print('There are more even numbers in the list')
elif len(odd) > len(even):
    print('There are more odd numbers in the list')
else:
    print('The list includes the equal number the even and odd numbers')
# g) print the list's product (the multiplication of all values in the list)
if len(numbers) > 0:
    p = 1
else:
    p = 0
for n in numbers:
    p *= n
print('g) ', p)
# h) challenge: print the median (note that you need to consider if the list's length is
#     even or odd).
mean = None
if len(numbers) % 2 != 0:
    mean = numbers[len(numbers) // 2]
else:
    mean = (numbers[int(len(numbers) / 2)] + numbers[int(len(numbers) / 2) - 1]) / 2
print('h)', mean)
