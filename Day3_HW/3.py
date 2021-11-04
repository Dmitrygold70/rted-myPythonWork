"""
    a) Create a list of pairs username & password. create a simple terminal login
    interface (you can use getpass.getpass() to read password without printing the
    input)
    b) Do the same but replace the list with a dictionary (with username as the key)
"""
import getpass

accounts = [('u', 'p'), ('u1', 'p1')]
accounts_dict = {'u': 'p', 'u1': 'p1'}

user = input('Please enter the user name: ')
pwd = getpass.getpass('User name: %s, please enter the password: ' % user)
# a
if (user, pwd) in accounts:
    print('\nWelcome')
else:
    print('\nThe password is incorrect')
# b
if accounts_dict.get(user) == pwd:  # Use get for elimination the exception if the user name is not in the dict.keys()
    print('\nWelcome')
else:
    print('\nThe password is incorrect')
