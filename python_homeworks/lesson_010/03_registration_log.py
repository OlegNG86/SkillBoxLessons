# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


class FileChecker:

    def __init__(self, name):
        self.name = name
        self.data = None
        self.user_age = None
        self.user_age_check = 10 > self.user_age > 99
        self.user_name = None
        self.user_name_check = str.isalpha(self.user_name)
        self.user_email = None
        self.user_email_check = '@' and '.' in self.user_email

    def __str__(self):
        return f'Запущен файл {self.name}'

    def open_file(self):
        with open(self.name, 'r', encoding='utf8') as f:
            self.data = f.read()
        return self.data

    def check_file(self):
        if not self.user_name_check:
            raise NotNameError('В имени не только буквы.')
        if not self.user_email_check:
            raise NotEmailError('Адрес почты указан некорректно.')
        if not self.user_age_check:
            raise ValueError('Возраст указан некорректно.')

        try:
            for self.user_name, self.user_email, self.user_age in self.data.split(sep=' '):
                print(self.user_name)
        except:
            print('Была ошибка')

file_name = 'registrations.txt'
file1 = FileChecker(file_name)
file1.open_file()
file1.check_file()
