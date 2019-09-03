# -*- coding: utf-8 -*-
import calendar

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом

user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)

if 0 < month < 13:
    print('Вы ввели', month)
    monthrange = calendar.monthrange(2019, month)
    number_of_day = monthrange[1]
    print(number_of_day)
else:
    print('Месяцев всего 12, вы ввели неверное значение!')