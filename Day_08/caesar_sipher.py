alphabete = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def main():
    welcome()


def welcome():
    user_choose = input(print('Hello user. Today we gonna encode an decode caesar sipher. Please choose what you wanna do by input "decode" or "encode"'))
    choose_check(user_choose)


def choose_check(user_choose):
    if user_choose == 'decode':
        cypher_decode()
    else:
        cypher_encode()


def cypher_decode():
    word = input(print('please print word what you want decode'))
    word_list = []
    for letter in word:
        word_list += alphabete[(alphabete.index(letter) - 3)]
    print(word_list)
    continue_ask()


def cypher_encode():
    word = input(print('please print word what you want encode'))
    word_list = []
    for letter in word:
        letter_index = alphabete.index(letter) + 3
        if letter_index > len(alphabete):
            letter_index = letter_index - len(alphabete)
        word_list += alphabete[letter_index]
    print(word_list)
    continue_ask()


def continue_ask():
    user_choice = input('Want to continue? "yes" "no"')
    if user_choice == 'yes':
        manipulation_choice()


def manipulation_choice():
    user_choice = input('Please choose by input "decode" or "encode"')
    if user_choice == 'decode':
        cypher_decode()
    else:
        cypher_encode()


main()