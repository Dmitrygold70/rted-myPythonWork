x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("before: ", x)

for sublist in x:
    sublist.append(777)

print("after : ", x)
