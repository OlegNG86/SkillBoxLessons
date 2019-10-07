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
import operator
from pprint import pprint


class Book:
    total_sum = 0

    def __init__(self, name, encoding):
        self.name = name
        self.text_from_pushkin = None
        self.encoding = encoding

    def read(self):
        with open(self.name, 'r', encoding=self.encoding) as self.opened_file:
            self.text_from_pushkin = self.opened_file.read()
            return self.text_from_pushkin

    def char_count(self):
        char_dict = {}
        for i in range(1040, 1104):
            char = chr(i)
            char_count = self.text_from_pushkin.count(char)
            char_dict[char] = char_count
        return char_dict

    def sum_all_char(self):
        sum_all_char = 0
        for i in range(1040, 1104):
            char = chr(i)
            char_count = self.text_from_pushkin.count(char)
            sum_all_char += char_count
        return sum_all_char


folder = os.getcwd()
file_name_pushkin = 'pushkin.txt'
file_name_voina = 'voyna-i-mir.txt'

file_folder = 'python_snippets'
fullpath_pushkin = os.path.join(folder, file_folder, file_name_pushkin)
fullpath_voina = os.path.join(folder, file_folder, file_name_voina)

pushkin_file = Book(fullpath_pushkin, 'utf8')
voina_i_mir = Book(fullpath_voina, 'cp1251')
pushkin_file.read()
voina_i_mir.read()

# print(pushkin_file.char_count())
# print(pushkin_file.sum_all_char())
#
# print(voina_i_mir.char_count())
# print(voina_i_mir.sum_all_char())

print('+---------+----------+')
print('|  буква  | частота  |')
print('+---------+----------+')

for k, v in voina_i_mir.char_count().items():
    print(f'|{k:^9}|{v:^10}|')

print('+---------+----------+')
print(f'|  итого  | {voina_i_mir.sum_all_char()}  |')
print('+---------+----------+')

#  - по частоте по возрастанию
sorted_x = sorted(voina_i_mir.char_count().items(), key=operator.itemgetter(1), reverse=False)
print(sorted_x)

#  - по алфавиту по возрастанию
sorted_x = sorted(voina_i_mir.char_count().items(), key=operator.itemgetter(0), reverse=False)
print(sorted_x)

#  - по алфавиту по убыванию
sorted_x = sorted(voina_i_mir.char_count().items(), key=operator.itemgetter(0), reverse=True)
print(sorted_x)



# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
