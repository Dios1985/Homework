# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
name = ''
age = 0
phone = ''
email = ''
index = ''
adress = ''
information = ''

# buisness information
OGRNIP = 0
INN = 0
RS = 0
Bank_name = ''
BIK = 0
KS = 0


def general_info_user(name_parameter, age_parameter, phone_parameter, email_parameter, index_parameter,
                      adress_parameter, information_parameter):
    print(SEPARATOR)
    print('Имя:    ', name_parameter)

    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', phone_parameter)
    print('E-mail: ', email_parameter)
    print('Индекс: ', index_parameter)
    print('Адрес: ', adress_parameter)
    if information:
        print('')
        print('Дополнительная информация:')
        print(information_parameter)


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                name = input('Введите имя: ')
                while 1:
                    # validate user age
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    print('Возраст должен быть положительным')

                phone_number = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone = ''
                for ch in phone_number:
                    if ch == '+' or ('0' <= ch <= '9'):
                        phone += ch

                email = input('Введите адрес электронной почты: ')
                index_input = input('Введите почтовый индекс: ')
                index = ''
                for symbol in index_input:
                    if '0' <= symbol <= '9':
                        index += symbol

                adress = input('Введите почтовый адрес (без индекса): ')
                information = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input social links
                while 2:
                    OGRNIP = input('Введите ОГРНИП: ')
                    count = 0
                    for symbol in OGRNIP:
                        count += 1
                    if count == 15:
                        break
                    print('ОГРНИП должен содержать 15 цифр')
                INN = input('Введите ИНН: ')

                while 2:
                    RS = input('Введите расчетный счет: ')
                    count = 0
                    for symbol in RS:
                        count += 1
                    if count == 20:
                        break
                    print('Расчетный счет должен содержать 20 цифр')

                Bank_name = input('Введите название банка: ')
                BIK = int(input('Введите БИК: '))
                KS = int(input('Введите корреспондентский счет: '))
            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(name, age, phone, email, index, adress, information)

            elif option2 == 2:
                general_info_user(name, age, phone, email, index, adress, information)

                # print social links
                print('')
                print('Информация о предпринимателе')
                print('ОГРНИП:', OGRNIP)
                print('ИНН: ', INN)
                print('Банковские реквизиты')
                print('Р/с:   ', RS)
                print('Банк: ', Bank_name)
                print('БИК: ', BIK)
                print('К/с: ', KS)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')