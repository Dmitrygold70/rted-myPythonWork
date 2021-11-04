print("""
    Menu Title:
    -----------
    1) Action One
    2) Action Two
    3) Action Three
    0) Quit
""")

option = input("Enter option:")

if option == '1':
    print("Performing Action One...")
elif option == '2':
    print("Performing Action Two...")
elif option == '3':
    print("Performing Action Three...")
elif option == '0':
    print("Quitting Time...")
else:
    print("Invalid Option!")

