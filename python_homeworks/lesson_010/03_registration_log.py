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


class ValueError(Exception):
    pass


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


class FileChecker:

    def __init__(self, name):
        self.name = name
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
            data = f.read()
        return data

    def check_file(self):
        pass


file_name = 'registrations.txt'
file1 = FileChecker(file_name)
print(file1.open_file())
