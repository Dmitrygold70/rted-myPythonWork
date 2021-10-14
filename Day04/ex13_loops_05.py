x = [10, 20, 30, 40, 50, 60]

print("before: ", x)

for num in x:
    num += 5  #won't change x

print("after : ", x)

# ints are immutable
# n += m --> n = n + m
# creating a copy.
