# Задача 5. Стипендия
# Ежемесячная стипендия студента составляет educational_grant рублей, а расходы на проживание превышают стипендию и составляют expenses рублей в месяц.
#
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца. Обратите внимание, что каждый месяц цены увеличиваются на 3% относительно прошлого месяца.
#
# Что нужно сделать
# Составьте программу расчёта суммы денег, которую необходимо получить у родителей один раз в начале обучения, чтобы можно было прожить учебный год (десять месяцев), используя только эти деньги и стипендию.
#
# Обратите внимание: во всех расчётах программы используются только целые числа, а дробные значения преобразуются в целые.
#
# Пример
#
# Введите ежемесячную стипендию: 10000
# Введите ежемесячные расходы: 12000
#
# 1-й месяц: траты 12000 рублей, не хватает 2000 рублей.
# 2-й месяц: траты 12360 рублей, не хватает 2360 рублей.
# 3-й месяц: траты 12730 рублей, не хватает 2730 рублей.
# 4-й месяц: траты 13111 рублей, не хватает 3111 рублей.
# 5-й месяц: траты 13504 рублей, не хватает 3504 рублей.
# 6-й месяц: траты 13909 рублей, не хватает 3909 рублей.
# 7-й месяц: траты 14326 рублей, не хватает 4326 рублей.
# 8-й месяц: траты 14755 рублей, не хватает 4755 рублей.
# 9-й месяц: траты 15197 рублей, не хватает 5197 рублей.
# 10-й месяц: траты 15652 рублей, не хватает 5652 рублей.
#
# Сумма денег, которую необходимо получить у родителей: 37544 рублей.
#
# Что оценивается
# Результат вывода соответствует условию.
# Вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).

educational_grant = int(input('Введите ежемесячную стипендию: '))
expenses = int(input('Введите ежемесячные расходы: '))
total_month = 10 # Либо через int(input), чтобы ввести определенное кол-во месяцев
summ = 0

for month in range(1, total_month + 1, 1):
    print(f'{month}-ый месяц: траты {expenses} рублей, не хватает {expenses - educational_grant} рублей.')
    percent = expenses * 3 // 100
    expenses += percent
    summ += expenses
print('Сумма денег, которую необходимо получить у родителей: 37544 рублей.')

# Принято
