# Задание 5. Наибольшая сумма цифр
# Что нужно сделать
# Пользователь вводит N чисел. Среди натуральных чисел, которые он указал, найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.
#
# Пример
# Введите количество чисел: 3
# Введите число: 5
# Введите число: 98
# Введите число: 453
#
# Число 98 имеет максимальную сумму цифр: 17
#
# Что оценивается
# Результат вывода соответствует условию.
# Вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).

total_number = int(input('Введите количество чисел: '))
total_summ = 0
summ = 0
max_number = 0
for num in range(total_number):
    number = int(input('Введите число: '))
    current = number
    while number != 0:
        summ += number % 10
        number //= 10
    if summ > total_summ:
        total_summ = summ
        max_number = current
    summ = 0

print('Число', max_number, 'имеет максимальную сумму цифр:', total_summ)

# Принято
