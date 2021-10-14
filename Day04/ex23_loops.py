x = [1, 2, 702, 704, 3, 4, 804, 806, 808]

print("before removing:", x)
print("sorted to help us see:", sorted(x))

# if a number is greater than 300 and even, remove it.
i = 0
while i < len(x):
    if x[i] > 300 and x[i] % 2 == 0:
        del x[i]
        continue

    i += 1

print("after removing:", x)
