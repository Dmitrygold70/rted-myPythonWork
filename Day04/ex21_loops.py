x = [1, 2, 702, 704, 3, 4, 804, 806, 808]

print("before removing:", x)
print("sorted to help us see:", sorted(x))

# if a number is greater than 300 and even, remove it.
for num in x:
    if num > 300 and num % 2 == 0:
        # won't work. you can't change a list while iterating it
        x.remove(num)

print("after removing:", x)
