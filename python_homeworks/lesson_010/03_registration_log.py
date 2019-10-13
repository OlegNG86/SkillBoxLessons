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

import re


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


class FileChecker:

    def __init__(self, name):
        self.name = name
        self.new_name_file = None
        self.data = None
        self.user_age = None
        self.user_age_check = r'\b[1-9]{1}[0-9]{1}'
        self.user_name = None
        self.user_name_check = r'\b[A-Z]*[A-z]*[А-Я]*[А-я]*'
        self.user_email = None
        self.user_email_check = r'\b[a-z]*[.]*[a-z]*@\w*\.\w*'
        self.pattern = re.compile(self.user_name_check+str([ ])+self.user_email_check+str([ ])+self.user_age_check)

    def __str__(self):
        return f'Запущен файл {self.name}'

    def open_file(self):
        with open(self.name, 'r', encoding='utf8') as f:
            self.data = f.readlines()
        return self.data

    def write_new_file(self, newnamefile, data):
        self.new_name_file = newnamefile
        self.data = data
        with open(self.new_name_file, 'w', encoding='utf8') as f:
            f.writelines(self.data)

    def check_file(self):
        # bad_list = []

            for i in self.data:
                try:

                    if len(re.split(' ', i)) == 3:
                        self.user_name, self.user_email, self.user_age = re.split(' ', i)
                        # print(self.user_email)
                        self.user_name = re.findall(self.user_name_check, self.user_name)
                        self.user_age = re.findall(self.user_age_check, self.user_age)
                        self.user_email = re.findall(self.user_email_check, self.user_email)
                        print(len(self.user_name), len(self.user_email), len(self.user_age))
                        # self.user_name, self.user_email, self.user_age = i.split(sep=' ')
                        # print(self.user_name if self.user_name_check.search(self.user_name) != None)
                        # if len(i.split(sep=' ')) != 3:
                        #     raise ValueError('Не присутствуют все три поля')

                            # if not self.user_name_check == False:
                            #     raise NotNameError('В имени не только буквы.')
                            # if not self.user_email_check == False:
                            #     raise NotEmailError('Адрес почты указан некорректно.')
                            # if not self.user_age_check == False:
                            #     raise ValueError('Возраст указан некорректно.')
                        # else:
                        #     bad_list.append(i)


                except Exception as exc:
                    print(f'Была ошибка {exc}')

                finally:
                    pass
                    # self.write_new_file('registrations_bad.log', bad_list)


    def print_strings(self):
        count = 0
        for i in self.data:
            count += 1
            print(type(i))
        print(count)


file_name = 'registrations.txt'
file1 = FileChecker(file_name)
file1.open_file()
file1.check_file()
# file1.print_strings()
