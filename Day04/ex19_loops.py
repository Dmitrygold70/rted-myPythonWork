import random

x = []

# add 10 random values from 1-1000 into x
for i in range(10):
    x.append(random.randint(1, 1000))

print(x)
print(sorted(x))

# for each number in x greater than 300 and the number is even, print it
for num in x:
    if num > 300 and num % 2 == 0:
        print(num)

