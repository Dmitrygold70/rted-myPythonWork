x = [
    (1, 100),
    (2, 200),
    (3, 300)
]

for pair in x:
    print("left: {}; right: {}".format(pair[0], pair[1]))

print("----------")

for left, right in x:
    # left, right = x[i]
    print("left: {}; right: {}".format(left, right))

