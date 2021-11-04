# 1. Write a Python script to sort (ascending and descending) a dictionary by value.


# 2. Write a Python script to add a key to a dictionary.
#     Sample Dictionary : {0: 10, 1: 20}
#     Expected Result : {0: 10, 1: 20, 2: 30}


# 3. Write a Python script to concatenate following dictionaries to create a new one.
#     Sample Dictionary :
#     dic1={1:10, 2:20}
#     dic2={3:30, 4:40}
#     dic3={5:50,6:60}
#     Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def dict_concatenate(*args):
    dc = dict()
    for d in args:
        dc.update(d)
    return dc
# print(dict_concatenate({1:10, 2:20},{3:30, 4:40}, {5:50,6:60}))


# 6. Write a Python script to generate and print a dictionary
#     that contains a number (between 1 and n) in the form (x, x*x).
#     Sample Dictionary ( n = 5) :
#     Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
def key_pow_2(i):
    d = {}
    for i in range(1, i + 1):
        d[i] = i**2
    return d
# print(key_pow_2(5))


# 8. Write script to merge two Python dictionaries.
def dict_merge(*args):
    merged_d = dict()
    for dictionary in args:
        merged_d.update(dictionary)
    return merged_d

# 9. Write program to iterate over dictionaries using for loops.


# 10. Write  program to sum all the items in a dictionary.
def sum_dict_val(dict1: dict):
    return sum(dict1.values())


# 11. Write  program to multiply all the items in a dictionary.
def mlt_dict_val(dict1: dict):
    mlt = 1
    for v in dict1.values():
        mlt *= v
    return mlt
# print('mlt', mlt_dict_val({'a': 1, 2:2, 3:3}))
