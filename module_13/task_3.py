# Задача 3. Число наоборот
# Что нужно сделать
# Пользователь вводит два числа: N и K.
#
# Напишите программу, которая переворачивает каждое из введённых чисел, то есть записывает эти числа в обратном порядке.
#
# Пример
#
# Введите первое число: 102
# Введите второе число: 123
#
# Первое число наоборот: 201
# Второе число наоборот: 321
#
# Что оценивается
# Задача решена с использованием функции, которая переворачивает число.
# Результат вывода соответствует условию, а формат вывода соответствует примеру.
# Вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).


def reverse_number(number):
    summ = ''
    if number < 0:
        return 0
    while number != 0:
        last_number = number % 10
        summ += str(last_number)
        number //= 10
    return summ


# TODO в этой функции нет проверки на то, что число неотрицательное как будто бы нет смысла,
#  просто 2 раза вызовите reverse_number в основном коде
def reverse(first, second):
    # TODO не информативное имена параметров
    first_reverse_number = reverse_number(first)
    second_reverse_number = reverse_number(second)
    return first_reverse_number, second_reverse_number


first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
first_reverse_number, second_reverse_number = reverse(first, second)

print('Первое число наоборот: ', first_reverse_number)
print('Второе число наоборот: ', second_reverse_number)
