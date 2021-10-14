'''
You are given the following strings:
Str1 = “abcdefghijklmnopqrstuvwxyz”
Str2 = “012123234345456567678789”
Str3 = “010203040506070809”
Str4 = “”
Assign to Str4 the following:
 All the letters from Str1 starting from the second letter, ending in one before last.
 Add to Str4 the slice from Str1 for every third letter starting the second letter.
 Add to Str4 the slice from str3 for every second letter in reverse.
'''


Str1 = 'abcdefghijklmnopqrstuvwxyz'
Str2 = '012123234345456567678789'
Str3 = '010203040506070809'

#  All the letters from Str1 starting from the second letter, ending in one before last.
Str4 = Str1[1:-2]
print(Str4)

#  Add to Str4 the slice from Str1 for every third letter starting the second letter
Str4 = Str1[1::3]
print(Str4)

#  Add to Str4 the slice from str3 for every second letter in reverse.
Str4 = Str3[-1:0:-1]
print(Str4)
