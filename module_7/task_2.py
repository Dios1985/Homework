print('Задача 2. Посчитай чужую зарплату...')

# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании и, чтобы облегчить себе жизнь, обратилась к программисту.

# Напишите программу, которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев
# и выводит на экран среднюю зарплату за год.

# Пример
# Введите зарплату сотрудника: 20000
# Введите зарплату сотрудника: 40000
# Введите зарплату сотрудника: 35000
# Введите зарплату сотрудника: 40000
# ....
# ....
# ....
# Средняя зарплата за год: 37916.6

summ = 0
for month in range(12):
    salary = int(input('Введите зарплату сотрудника: '))
    summ += salary
# TODO проблема в том, что вы используте переменную month, которая какждый раз меняется внутри цикла и переменную salary
#  Которая так же запрашивается каждый раз внутри цикла и по сути содержит только последнюю зарплату:
#  Например на последнем месяце зарплата составила 12000
#  А так как в переменной salary все прошлые значения не записанны (они у вас в другой переменной)
#  то фактически ваша итоговая формула будет выглядеть так :
#  average_salary = 12000 / (11 + 1) = 1000
#  В целом вам лучше вынести переменную month перед циклом month = 12
#  А сам цикл итерировать уже по этой переменной for _ in range(month):
#  Ну а с переменной где у вас сумма зарплаты думаю вы уже поняли)
average_salary = salary / (month + 1) # А если сделать так?
print('Средняя зарплата за год: ', average_salary)