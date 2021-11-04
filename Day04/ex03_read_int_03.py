print("Hello")

text = input("Enter an integer:")

if text[0] in "-0123456789" and text[1:].isdigit():
    num = int(text)
    print("your number is", num)
else:
    print("That's not in integer")

print("Goodbye")
