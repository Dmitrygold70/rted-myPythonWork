"""
Make a hangman game, create a list of single words of your desired topic,
the program pics one word at random and lets the user guess letters of the word
while showing the correct letters (revealed on the word itself) as well as the wrong letters.
(after the player is wrong 5 times or guesses the whole word, the game is over and the word is revealed)
"""
import random


def get_words_from_file(filename):
    words = list()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            words = words + [word.strip() for word in line.split(' ') if len(word) > 0]
    return words


def add_word_to_db(filename, word):
    with open(filename, 'a') as f:
        f.write(f'\n{word}')


def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x.lower() < lst[0].lower()])
            + [lst[0]] + quicksort([x for x in lst[1:] if x.lower() >= lst[0].lower()]))


def masking_word():
    global my_word, masking_bitmap
    for index in range(len(my_word)):
        if masking_bitmap[index] == 0:
            print('*', end='')
        else:
            print(my_word[index], end='')
    print()


def get_letter():
    global my_word, masking_bitmap, guess_error
    letter = input('Please enter the letter:\n>').lower().strip()
    if len(letter) > 1:
        if letter == my_word.lower():
            for i in range(len(my_word)):
                masking_bitmap[i] = 1
        else:
            guess_error += len(letter)
    for i in range(len(my_word)):
        if my_word[i].lower() == letter:
            masking_bitmap[i] = 1


db_file = 'words.txt'
menu = {'a': 'a) Add the word to the DB',
        'p': 'p) Play the game',
        'r': 'r) Remove the word from the DB',
        's': 's) show the words collection',
        'x': 'x) Exit'}

if __name__ == '__main__':
    while True:
        for k in menu:
            print(menu[k])
        choice = input('>').strip().lower()
        if choice not in menu:
            print('Incorrect input')

        if choice == 'a':
            word = input('Please enter the word to be added to the DB\n>').strip()
            add_word_to_db(db_file, word)

        elif choice == 'x':
            break

        elif choice == 's':
            word_lst = get_words_from_file(db_file)
            lst_sorted = quicksort(word_lst)
            for word in lst_sorted:
                print(word)

        elif choice == 'r':
            word_lst = get_words_from_file(db_file)
            word_to_remove = input('Please enter the word to be removed from the list: ').strip().lower()
            for i in range(len(word_lst)):
                if word_lst[i] == word_to_remove:
                    word_lst[i] = ''
            with open(db_file, 'w') as f:
                for word in word_lst:
                    if len(word) > 0:
                        f.write(f'{word}\n')

        elif choice == 'p':
            word_lst = get_words_from_file(db_file)
            rand_index = random.randint(0, len(word_lst) - 1)
            my_word = word_lst[rand_index]
            masking_bitmap = [0 for ch in my_word]
            guess_error = 0
            iswon = False
            print(my_word)
            while guess_error < 5:
                a = sum(masking_bitmap)
                masking_word()
                get_letter()
                if sum(masking_bitmap) == a:
                    guess_error += 1
                if sum(masking_bitmap) == len(my_word):
                    print('You WON!')
                    print()
                    iswon = True
                    break
            if not iswon:
                print('You Fail!')
                print()
