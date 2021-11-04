"""
Create a Guess-the-Number terminal game. the program picks a random number from a
range (for example 1-100) the user is then given several tries to guess the number (for
example 5) every wrong guess the program will print "too low" or "too high" respectively.
if the player guesses correctly, "you win" is printed and the game end), if there are zero
tries left "game over" is printed and the game ends. (extra: when the game end ask the
user if they want to play again)
"""
import random


def get_int():
    while True:
        isnum = True
        num = input('Please enter a number in range 1-100\n>').strip()
        for i in range(len(num)):
            if not num.isdigit():
                print('Incorrect input.')
                isnum = False
                break
        if isnum:
            return int(num)


if __name__ == '__main__':
    guess_num = random.randint(1, 100)
    incorrect_count = 0
    iswin = False
    while incorrect_count < 5:
        num = get_int()
        if num == guess_num:
            print('You Win')
            iswin = True
            break
        elif num < guess_num:
            print('Too low')
            incorrect_count += 1
        else:
            print('Too high')
            incorrect_count += 1
    if not iswin:
        print('Game over')
