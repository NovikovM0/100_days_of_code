auction_dictionary = {}


def main():
    welcome()
    auction_results()


def welcome():
    print('Welcome to secret auction game')
    add_participant()


def add_participant():
    name = input('Please input your name')
    bid = int(input('Please input your bid in $'))
    auction_dictionary[name] = bid
    print(f'participant added:\n{name}\n${bid}')
    new_participant_check()


def new_participant_check():
    user_choice = input('Any other bidder? Type "yes" or "no"')
    if user_choice == 'yes':
        add_participant()


def auction_results():
    winner = ''
    max_bed = 0
    for i in auction_dictionary:
        if auction_dictionary[i] > max_bed:
            max_bed = auction_dictionary[i]
            winner = i
    print(f'Winner of todays auction is {winner} with bed ${max_bed}. Congratulation!!!')


main()