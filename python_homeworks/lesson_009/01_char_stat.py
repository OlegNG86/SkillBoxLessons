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


folder = os.getcwd()
# file_name = 'voyna-i-mir.txt.zip'
file_name = 'pushkin.txt'

pushkin_folder = 'python_snippets'
fullpath = os.path.join(folder, pushkin_folder, file_name)

with open(fullpath, 'r', encoding='utf8') as opened_file:
    text_from_pushkin = opened_file.read()
    print(text_from_pushkin)

sum_all_char = 0
char_dict = {}

for i in range(1040, 1104):
    char = chr(i)
    char_count = text_from_pushkin.count(char)
    sum_all_char += char_count
    char_dict[char] = char_count
print(char_dict)









# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
