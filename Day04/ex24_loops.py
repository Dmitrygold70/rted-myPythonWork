x = [1, 2, 702, 704, 3, 4, 804, 806, 808]

is_number_found = False
number_found = None

# find and print the first number that is greater than 300
for num in x:
    if num > 300:
        is_number_found = True
        number_found = num
        break

if is_number_found:
    print("number found:", number_found)
else:
    print("number not found")
