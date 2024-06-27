def addition(num_1, num_2):
    return num_1 + num_2


def subtraction(num_1, num_2):
    return num_1 - num_2


def multiplication(num_1, num_2):
    return num_1 * num_2


def division(num_1, num_2):
    return num_1 / num_2


operations = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division
}


def main():
    welcome()


def welcome():
    print('Welcome to calculator!')
    num_1 = int(input('Please type first number'))
    num_2 = int(input('Please type second number'))
    print('Please choose operation from that list:')
    for i in operations:
        print(i)
    operation = input()
    operation_function = operations[operation]
    result = operation_function(num_1, num_2)
    print(result)
    while result != False:
        result = continue_ask(result)


def continue_ask(result):
    user_choice = input(f'Type "y" to continue manipulate with {result}, or "n" to exit')
    if user_choice == 'y':
        return continue_operations(result)
    else:
        return False


def continue_operations(num_1):
    num_2 = int(input('Please type second number'))
    print('Please choose operation from that list:')
    for i in operations:
        print(i)
    operation = input()
    operation_function = operations[operation]
    result = operation_function(num_1, num_2)
    print(result)
    return result


main()