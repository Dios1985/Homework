print('Задача 4. Отрезок')

# Напишите программу, которая считывает с клавиатуры два числа: a и b,
# считает и выводит в консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу 3.

# Подсказки:
# Средним арифметическим нескольких чисел называют сумму этих чисел, делённую на их количество.
# Кратность означает, что число делится на заданное без остатка.

# Пример
# Начало отрезка: -5
# Конец отрезка: 12
# Числа из отрезка, которые делятся на 3:
# -3
# 0
# 3
# 6
# 9
# 12
# Среднее арифметическое этих чисел: 4.5

start = int(input('Начало отрезка: '))
end = int(input('Конец отрезка: '))
summ = 0
count = 0

for number in range(start, end + 1):
    if number % 3 == 0:
        print(number)
        count += 1
        summ += number
        average_summ = summ / count
print('Среднее арифметическое этих чисел: ', average_summ)