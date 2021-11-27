'''
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''

previous_digit = 0
number = int(input('Введите целое положительное число >>> '))
while number > 0:
    current_digit = number % 10
    if current_digit > previous_digit:
        previous_digit = current_digit
    number = number // 10
print('Максималная цифра:', previous_digit)
