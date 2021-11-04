x = [1, 2, 702, 704, 3, 4, 804, 806, 808]
#x = [1, 2, 3]

# find and print the first number that is greater than 300
for num in x:
    if num > 300:
        print("number found:", num)
        break
else:  # if we didn't break - perform the else part.
    print("number not found")
