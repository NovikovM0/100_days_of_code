import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def main():
    player_choice = input('Hello player. Its rock paper scissor game! Please can you choose your move (print "rock, paper or scissor")').lower()
    player_choice = player_convertation(player_choice)
    bot_choice = bot_move()
    fight(player_choice, bot_choice)
def player_convertation(choice):
    if choice == 'rock':
        choice = rock
    elif choice == 'paper':
        choice = paper
    else:
        choice = scissor
    return choice
def bot_move():
    bot_random = random.randint(1,3)
    if bot_random == 1:
        bot_choice = rock
    elif bot_random == 2:
        bot_choice = paper
    else:
        bot_choice = scissor
    return bot_choice

def fight(player, bot):
    print(player)
    print(bot)
    if (player == rock and bot == scissor) or (player == paper and bot == rock) or (player == scissor and bot == paper):
        print('You won, congratulation')
    elif player == bot:
        print('Draw!')
    else:
        print('You lose, next time!')

main()