import random
card_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'x']
game_is_playing = True
alfred_turn_flag = True
bred_turn_flag = True
player_turn_flag = True


def main():
    art()
    welcome()
    game()


def game():
    alfred_hand = []
    bred_hand = []
    player_hand = []
    while game_is_playing:
        alfred_score = bot_alfred_turn(alfred_hand)
        bred_score = bot_bred_turn(bred_hand)
        player_score = player_turn(player_hand)
        game_check()
    final(alfred_score, bred_score, player_score)


def bot_alfred_turn(alfred_hand):
    global alfred_turn_flag
    alfred_number = 17
    print('Alfred turn')
    alfred_hand_number = hand_counting(alfred_hand)
    print(f'Alfred hand count {alfred_hand_number}')
    alfred_turn_flag = hand_check(alfred_hand_number, alfred_hand, alfred_number, alfred_turn_flag)
    print(alfred_hand)
    alfred_hand_number = hand_counting(alfred_hand)
    print(alfred_hand_number)
    return alfred_hand_number


def bot_bred_turn(bred_hand):
    global bred_turn_flag
    bred_number = 19
    print('Bred turn')
    bred_hand_number = hand_counting(bred_hand)
    print(f'Bred hand count {bred_hand_number}')
    bred_turn_flag = hand_check(bred_hand_number, bred_hand, bred_number, bred_turn_flag)
    print(bred_hand)
    bred_hand_number = hand_counting(bred_hand)
    print(bred_hand_number)
    return bred_hand_number


def player_turn(player_hand):
    global player_turn_flag
    print('Player turn')
    player_hand_number = hand_counting(player_hand)
    print(f'Your hand count {player_hand_number}')
    player_turn_flag = player_hand_check(player_hand_number, player_hand, player_turn_flag)
    print(player_hand)
    player_hand_number = hand_counting(player_hand)
    print(player_hand_number)
    return player_hand_number


def hand_counting(hand):
    hand_number = 0
    for card in hand:
        if isinstance(card, int):
            hand_number += card
        elif card != 'x':
            hand_number += 10
    if 'x' in hand:
        for i in range(hand.count('x')):
            if 21 - hand_number >= 11:
                hand_number += 11
            else:
                hand_number += 1
    return hand_number


def hand_check(hand_number, hand, bot_number, flag):
    if hand_number <= 16:
        hand.append(random.choice(card_deck))
        print('hit')
        return True
    elif hand_number == 21 :
        print('blackjack')
        return False
    elif hand_number >= 22 :
        print('bust')
        return False
    else:
        print('skip')
        return False


def player_hand_check(hand_number, hand, flag):
    if hand_number <= 21:
        if input('Do you want to take a card? type "yes" or "no"') == 'yes':
            print('hit')
            card = random.choice(card_deck)
            hand.append(card)
            input(f"you get {card} from deck, press any button")
            return True
        else:
            print('skip')
            return False
    elif hand_number == 21 :
        print('blackjack')
        return False
    elif hand_number >= 22 :
        print('bust')
        return False
    else:
        print('skip')
        return False


def game_check():
    global game_is_playing
    global alfred_turn_flag
    global bred_turn_flag
    global player_turn_flag
    if not alfred_turn_flag and not bred_turn_flag and not player_turn_flag:
        game_is_playing = False


def final(alfred_score, bred_score, player_score):
    winners = []
    results = {
    'Alfred': alfred_score,
    'Bred': bred_score,
    'Player': player_score
    }
    temp = 0
    for name, score in results.items():
        print(name, score)
        if score <= 21 and score > temp:
            winners = [name]
        elif score == temp:
            winners.append(name)
    print(f'Winners - {winners}')


def art():
    print('''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ simple ver.
                       _/ |                
                      |__/                 
''')


def welcome():
    print('Welcome to "Blackjack game". Here you gonna play vs 2 bots')


main()