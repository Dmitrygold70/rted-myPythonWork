'''
Complete the following
a. Print as requested in two different ways: num = input(“please enter a number: ”)
txt = input(“please enter a message: “)
print ___________ # print the number and the text
print ___________ # print the text and the number
b. You are given two numbers. Print the sum (+), difference (-),
multiplication (*), integer division, integer modulus,
float division and power between them.
c. Print three random numbers between 1 and 100.
Also print three random numbers between 0 and 1.
d. Print weather the text is palindrome txt = input(“please enter a message”)
print “result for palindrome test: “, _________
'''
# a) print the number and the text in two different ways
import random

num = int(input('please enter a number: '))
txt = input('please enter a message: ')
print(str(num), txt)
print(txt, str(num))

# b)You are given two numbers.
num1 = int(input("please enter the number: "))
num2 = int(input("please enter the number: "))
print(num1 + num2)
print(num1 - num2)
print(num1 // num2)
print(int(num1 % num2))
print(num1 / num2)
print(num1 ** num2)

# c)Print three random numbers between 1 and 100.
# Also print three random numbers between 0 and 1.
print(random.randrange(101), random.randrange(101), random.randrange(101))
print(random.randrange(2), random.randrange(2), random.randrange(2))

# d) Print weather the text is palindrome txt = input(“please enter a message”)
# print “result for palindrome test: “, _________
txt = input('please enter a message: ')
print(f'result for palindrome test: {txt[::-1]}')
