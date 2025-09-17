# Постарайтесь разделить логику кода на три отдельные логические части (функции):
#
# count_numbers — получает число и возвращает количество цифр в числе;
# change_number — получает число, меняет в нём местами первую и последнюю цифры и возвращает изменённое число;
# main — функция ничего не получает на вход, внутри запрашивает нужные данные от пользователя, выполняет дополнительные проверки и вызывает функции 1 и 2 для выполнения задачи (проверки и изменения двух чисел).
# Что нужно сделать
# Разбейте приведённую ниже программу на функции. Повторений кода должно быть как можно меньше. Также сделайте, чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.

# first_n = int(input("Введите первое число: "))
# first_num_count = 0
# temp = first_n
# while temp > 0:
#     first_num_count += 1
#     temp = temp // 10
#
# if first_num_count < 3:
#     print("В первом числе меньше трёх цифр.")
# else:
#     last_digit = first_n % 10
#     first_digit = first_n // 10 ** (first_num_count - 1)
#     between_digits = first_n % 10 ** (first_num_count - 1) // 10
#     first_n = last_digit * 10 ** (first_num_count - 1) + between_digits * 10 + first_digit
#     print('Изменённое первое число:', first_n)
#     second_n = int(input("\nВведите второе число: "))
#     second_num_count = 0
#     temp = second_n
#
#     while temp > 0:
#         second_num_count += 1
#         temp = temp // 10
#     if second_num_count < 4:
#         print("Во втором числе меньше четырёх цифр.")
#     else:
#         last_digit = second_n % 10
#         first_digit = second_n // 10 ** (second_num_count - 1)
#         between_digits = second_n % 10 ** (second_num_count - 1) // 10
#         second_n = last_digit * 10 ** (second_num_count - 1) + between_digits * 10 + first_digit
#         print('Изменённое второе число:', second_n)
#         print('\nСумма чисел:', first_n + second_n)
# Что оценивается
# Программа разбита на несколько функций.
# Выполнены условия по организации основного тела программы.
#
# Решение:

def main():
    # TODO вам нужно только 3 функции: main, count_numbers и функция для изменения числа
    first_n = int(input("Введите первое число: "))
    first_num_count = count_numbers(first_n)

    if first_num_count < 3:  # TODO если в числе меньше 3 цифр, то не нужно запрашивать второе число
        print("В первом числе меньше трёх цифр.\f")
        main()

    second_n = int(input("\nВведите второе число: "))
    second_num_count = count_numbers(second_n)

    if second_num_count < 4:
        print("Во втором числе меньше четырёх цифр.\f")
        main()

    first_n = change_number(first_n, first_num_count, 3, 'первое')
    second_n = change_number(second_n, second_num_count, 4, 'второе')

    print('\nСумма чисел:', first_n + second_n)


def count_numbers(count):
    num_count = 0
    temp = count
    while temp > 0:
        num_count += 1
        temp = temp // 10
    return num_count


def change_number(number, num_count, total_count, name):
    # TODO код дублируется с фунцией change_second_number
    last_digit = number % 10
    first_digit = number // 10 ** (num_count - 1)
    between_digits = number % 10 ** (num_count - 1) // 10
    number = last_digit * 10 ** (num_count - 1) + between_digits * 10 + first_digit
    print('Изменённое', name, 'число:', number)
    return number

# TODO после функции должны быть 2 пустые строчки
main()