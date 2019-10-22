# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

def generator(file, group_by):
    counter = 0
    with open(file, 'r', encoding='utf-8') as f:
        for i in f:
            if group_by in i:
                counter += 1
                a, b, c = i.split()
                yield a[1:] + ' ' + b[:5], counter


filename = 'events.txt'
group_by = 'NOK'

gen = generator(filename, group_by)

grouped_events = generator(filename, group_by)
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
