import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
password_list = []
password = ''

letters_amount = int(input('How many letters you wanna see in your password?'))
symbols_amount = int(input('How many symbols you wanna see in your password?'))
numbers_amount = int(input('How many numbers you wanna see in your password?'))
i = 1
j = 1
k = 1

while i <= letters_amount:
    password_list.append(letters[random.randint(0, len(letters)-1)])
    i += 1
while j <= symbols_amount:
    password_list.append(symbols[random.randint(0, len(symbols)-1)])
    j += 1
while k <= numbers_amount:
    password_list.append(numbers[random.randint(0, len(numbers)-1)])
    k += 1
print(password_list)
for i in range(0, len(password_list)):
    password += password_list.pop(random.randint(0, len(password_list)-1))
print(password)