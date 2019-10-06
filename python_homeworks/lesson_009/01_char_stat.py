# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import os
from pprint import pprint


class Book:

    def __init__(self, name):
        self.name = name
        self._text_from_book = None
        self._opened_file = None

    def format(self):
        pass

    def open(self):
        pass

    def read(self):
        with open(self.name, 'r', encoding='utf8') as self._opened_file:
            self._text_from_book = self._opened_file.read()
            print(self._text_from_book)

    def char_count(self):
        pass

    def char_sum(self):
        pass


folder = os.getcwd()
# file_name = 'voyna-i-mir.txt.zip'
file_name = 'pushkin.txt'

pushkin_folder = 'python_snippets'
fullpath = os.path.join(folder, pushkin_folder, file_name)

pushkin_book = Book(fullpath)
pushkin_book.open()
pushkin_book.read()

# with open(fullpath, 'r', encoding='utf8') as opened_file:
#     text_from_pushkin = opened_file.read()
#     print(text_from_pushkin)

# sum_all_char = 0
# char_dict = {}
#
# for i in range(1040, 1104):
#     char = chr(i)
#     char_count = text_from_pushkin.count(char)
#     sum_all_char += char_count
#     char_dict[char] = char_count
# print(char_dict)


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
