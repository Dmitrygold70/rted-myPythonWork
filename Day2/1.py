
def get_name(mystring):
    for i in range(len(mystring)):
        if mystring[i].isdigit():
            return mystring[:i]
    return mystring


# name = 'moshe765_kkdjfhhs'
# print(get_name(name))

a = dict()
a[0] = 'zero'
a[1] = 'one'
print(a)
print(a.items())
