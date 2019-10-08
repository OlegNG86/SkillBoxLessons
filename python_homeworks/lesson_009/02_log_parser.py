# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import datetime
from itertools import groupby


class CountFile:
    count = 0
    newlist = []

    def __init__(self, name, other_name, sort_parameter):
        self.name = name
        self.other_name = other_name
        self.sort_parameter = sort_parameter

    def sort(self):
        with open(self.name, 'r') as f:
            for i in f.readlines():
                k, j = i.strip().replace('[', '').split('] ')
                if j == self.sort_parameter:
                    constant = k[:16]
                    CountFile.count += 1
                    if constant not in CountFile.newlist:
                        CountFile.newlist.append(f'[{constant}] {CountFile.count}')
        return CountFile.newlist

    def show_sort(self):
        for i in CountFile.newlist:
            print(i)

    def write_file(self):
        with open(self.other_name, 'w') as f:
            for i in CountFile.newlist:
                f.writelines(i + '\n')


file = CountFile('events.txt', 'otherfile.txt', 'NOK')
file.sort()
file.show_sort()
file.write_file()


# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
