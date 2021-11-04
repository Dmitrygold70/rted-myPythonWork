x = [10, 20, 30]

print(x)

# enumerate creates an iterator of index value pairs: (0,10) , (1,20) ...
for i, v in enumerate(x):
    x[i] = v + 5

print(x)
