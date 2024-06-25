import random
from datetime import datetime

from_number = 0
to_number = 0
health = 0

def main():
    if input(
            'Приветствую тебя в угадайке! Не хочешь попробовать свои силы? (Введи "да", если хочешь сыграть)\n').lower() in [
        'да', 'lf']:
        rules()
    else:
        if input('Ты уверен что не хочешь сыграть? Если передумал напиши "нет"\n').lower() in ['нет', 'ytn']:
            rules()
        else:
            surrender()

# region основная часть игры

def new_run():
    if input('Хочешь сыграть снова? (Введи "да", если хочешь сыграть)\n').lower() not in ['да', 'lf']:
        return
    from_number = random.randint(0, 50)
    to_number = random.randint(50, 100)
    health = random.randint(1, 10)
    print('Смотри, я короче загадываю число от', from_number, 'до', to_number, 'и ты должен угадать его за', health,
          word_convertation(health))
    if input(
            'А теперь напиши "готов", если ты готов к игре или напиши что-нибудь другое, если хочешь закончить игру\n').lower() in [
        'готов', 'ujnjd']:
        game(from_number, to_number, health)
    else:
        surrender()
    return


def rules():
    from_number = random.randint(0, 50)
    to_number = random.randint(50, 100)
    health = random.randint(1, 10)
    print('Отлично! Давай я объясню тебе правила')
    print('Смотри, я короче загадываю число наример ... от', from_number, 'до', to_number, 'и ты должен угадать его за',
          health, word_convertation(health))
    if input(
            'А теперь напиши "готов", если ты готов к игре или напиши что-нибудь другое, если хочешь закончить игру\n').lower() in [
        'готов', 'ujnjd']:
        game(from_number, to_number, health)
    else:
        surrender()
    return


def game(from_number, to_number, health):
    speedrun_phrases = ['Да ты спидранер! Поздравляю с такой уверенной победой',
                        'Вот это скорость😳, сегодня точно в казино!',
                        'Ого-го-го какие мы быстрые, может на битву экстрасенсов?']
    normalrun_phrases = ['Молодец, хорошая игра!', 'Ты чертовски прав, отлично сыграно',
                         'Мега-хорош, поздравляю с победой']
    slowrun_phrases = ['Да уж, лучше поздно чем никогда😅',
                       'Тебе определенно нужно где-то прокачать свои экстрасенсорные способности',
                       'Кажется я вздремнул пока ты искал ответ🥱, в любом случае - спасибо за игру']
    miss_high = ['Слишком высоко, надро брать пониже', 'Чел, бери ниже', 'Надо выбрать число поменьше']
    close_miss_high = ['Ты близко! Возьми немного ниже', 'Очень горячо, выбери число поменьше',
                       'Тепло-тепло, осталось спуститься немного ниже']
    miss_low = ['Слишком низко, надро брать повыше', 'Чел, бери выше', 'Надо выбрать число побольше']
    close_miss_low = ['Ты близко! Возьми немного выше', 'Очень горячо, выбери число побольше',
                      'Тепло-тепло, осталось забраться немного выше']
    so_close = ['А-А-А-А ГОРЯЧО!!!', 'МНЕ КАЖЕТСЯ МЫ В ЖЕРЛЕ ВУЛКАНА', 'ЯДРО ЗЕМЛИ ДАЖЕ БЛИЗКО НЕ ТАКОЕ ТЕПЛОЕ']
    right_number = random.randint(from_number, to_number + 1)
    print(f'В общем у тебя {health} {word_convertation(health)}, удачи!')
    while health > 0:
        choosed_number = int(input())
        if choosed_number == right_number and health < 2:
            print(random.choice(speedrun_phrases))
            new_run()
            break
        elif choosed_number == right_number and 2 < health < 7:
            print(random.choice(normalrun_phrases))
            new_run()
            break
        elif choosed_number == right_number and 7 < health < 10:
            print(random.choice(slowrun_phrases))
            new_run()
            break
        else:
            if right_number - 1 < choosed_number < right_number + 1:
                print(random.choice(so_close))
                health -= 1
            elif right_number - 5 <= choosed_number < right_number:
                print(random.choice(close_miss_low))
                health -= 1
            elif choosed_number < right_number - 5:
                print(random.choice(miss_low))
                health -= 1
            elif right_number < choosed_number <= right_number + 5:
                print(random.choice(close_miss_high))
                health -= 1
            elif choosed_number > right_number + 5:
                print(random.choice(miss_high))
                health -= 1
    dead()
    new_run()
    return


# endregion

# region финал игры

def dead():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    sign = input('Ты погиб честью храбрых, оставь свою подпись: ')
    print('⣿⣿⡿⣫⣾⠏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣀⣀⣀⣀⠄⠄⠄⠄⠄⠄',
          '⣿⡇⠱⠉⠁⠄⠄⠄⠄⠄⠄⢀⣀⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣦⠄⠄⠄⠄⠄',
          '⣿⡇⠄⠄⠄⠄⠄⢀⣠⣛⡩⣩⣭⡹⣿⣿⣿⣿⠞⣛⣛⣛⡲⣿⡇⠄⠄⠄⠄',
          '⣿⡇⠄⠄⠄⡾⣡⣾⣿⣷⣹⣿⣿⡿⣪⡻⠟⣱⣿⣿⣿⣿⣿⣷⡹⠄⠄⠄⠄',
          '⣿⡇⠄⠄⣼⡇⣿⣻⣿⠟⡛⢿⣿⣾⣿⡇⢰⣍⢻⡿⠛⢿⣿⡭⣿⣷⠄⠄⠄',
          '⣿⣧⣄⡀⣿⡇⣮⣽⣿⣮⣉⣾⣿⣿⣿⣇⡸⣿⣿⣆⠛⣰⣿⣾⡿⣿⠄⠄⠄',
          '⣿⣇⡼⣄⣿⣿⡄⠙⢿⣏⣿⣿⡮⠁⣉⣾⣷⡈⠃⢿⣿⣬⡭⠝⣀⣿⠄⠄⠐',
          '⡆⡇⣹⣿⣿⣿⣿⡿⠓⠛⣉⣉⣉⣉⣙⣛⠓⠾⣟⢿⣿⣿⣿⣿⣿⣿⣿⠇⠄⠙',
          '⠁⡇⣞⣿⡿⠋⠁⠄⠄⠈⠉⠙⠛⠛⠻⠿⠿⠿⣶⣌⠻⣿⣿⣿⣿⣿⢗⢴⣆⢣',
          '⠸⣇⡻⠈⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢻⣷⡌⢿⣿⣿⣿⢸⠼⣣⣾',
          '⣦⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⠄⠄⠄⠄⠄⠄⠄⠄⠙⠛⠈⣿⡫⡼⢠⣾⣿⣿',
          '⣿⣇⠄⣀⣠⡀⠄⠄⠴⠾⠿⠿⠶⠶⣦⣤⡀⠄⠄⠄⠄⠄⠄⢨⠯⢁⣿⣿⣿⣿',
          f'⣿⣿⣦⢒⠤⣅⡶⣶⣶⣾⣿⣿⣿⣷⣶⣮⣍⠢⠄⠄⠄⠄⠄⠐⢠⣾⣿⣿⣿⣿ время смерти {current_time}',
          f'⣿⣿⣿⣧⡐⠫⣉⡿⣬⡞⢿⣿⢯⠽⣶⡽⢟⣛⢖⣨⣛⠛⢃⣴⣿⣿⣿⣿⣿⣿ {sign}', sep='\n')
    return


def surrender():
    print('Не очень то и хотелось 😡')


# endregion

# region Вспомогательные функции

def word_convertation(health):
    if health == 1:
        return 'попытку'
    elif 1 < health < 5:
        return 'попытки'
    else:
        return 'попыток'

main()