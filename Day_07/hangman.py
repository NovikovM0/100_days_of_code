import random

words = ['able', 'about', 'account', 'acid', 'across', 'act', 'addition', 'adjustment', 'advertisement', 'after', 'again', 'against', 'agreement', 'air', 'all', 'among', 'amount', 'amusement', 'and', 'angle', 'angry', 'animal', 'answer', 'ant', 'any', 'apparatus', 'apple', 'approval', 'arch', 'argument', 'arm', 'army', 'art', 'attack', 'attempt', 'attention', 'attraction', 'authority', 'automatic', 'baby', 'back', 'bad', 'bag', 'balance', 'ball', 'band']

def main():
    word = random.choice(words)
    word_letters = word_convertation(word)
    word_letters_final = word_convertation(word)
    underscore_word = underscore_convertation(word)
    lifes_amount = 6
    print('Welcome to hangman game!')
    print(word)
    print(underscore_word)
    while lifes_amount > 0:
        player_letter = input('Please input your letter')
        underscore_word = check_letter(player_letter, word_letters, underscore_word, lifes_amount)
        print(underscore_word)
        check_lifes(lifes_amount)
        if word_letters_final == underscore_word:
            good_ending()
            break


def word_convertation(word):
    word_list = []
    for letter in word:
        word_list += letter
    return word_list


def underscore_convertation(word):
    word_list = []
    for i in word:
        word_list += '_'
    return word_list


def check_lifes(lifes_amount):
    print(f'You have {lifes_amount} lifes')
    if lifes_amount < 0:
        bad_ending()


def check_letter(player_letter, word_letters, underscore_word, lifes_amount):
    if player_letter in word_letters:
        for i in range(word_letters.count(player_letter)):
            underscore_word[word_letters.index(player_letter)] = player_letter
            word_letters[word_letters.index(player_letter)] = '_'
    else:
        lifes_amount -= 1
    return underscore_word

def bad_ending():
    print('You loooooooose')

def good_ending():
    print('Good job!')

main()