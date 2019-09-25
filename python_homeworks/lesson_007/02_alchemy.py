# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Element:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __add__(self, other):
        if self.name == 'Сила' or other.name == 'Сила':
            if self.name == 'Воздух' or other.name == 'Воздух':
                return Element('Смерч')
            elif self.name == 'Огонь' or other.name == 'Огонь':
                return Element('Напалм')
            elif self.name == 'Земля' or other.name == 'Земля':
                return Element('Землятресение')
            elif self.name == 'Вода' or other.name == 'Вода':
                return Element('Наводнение')
        elif self.name == 'Вода' or other.name == 'Вода':
            if self.name == 'Воздух' or other.name == 'Воздух':
                return Element('Шторм')
            elif self.name == 'Огонь' or other.name == 'Огонь':
                return Element('Пар')
            elif self.name == 'Земля' or other.name == 'Земля':
                return Element('Грязь')

        elif self.name == 'Воздух' or other.name == 'Воздух':
            if self.name == 'Огонь' or other.name == 'Огонь':
                return Element('Молния')
            elif self.name == 'Земля' or other.name == 'Земля':
                return Element('Пыль')

        elif self.name == 'Огонь' or other.name == 'Огонь':
            if self.name == 'Земля' or other.name == 'Земля':
                return Element('Лава')

        else:
            return None


# class Water:
#
#     def __init__(self, name='Вода'):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def __add__(self, other):
#         if other.name == 'Воздух':
#             return Storm().name
#         elif other.name == 'Огонь':
#             return 'Пар'
#         else:
#             return None
#
#
# class Air:
#
#     def __init__(self, name='Воздух'):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def __add__(self, other):
#         if other.name == Water().name:
#             return Storm().name
#
#
# class Storm:
#
#     def __init__(self, name='Шторм'):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def __add__(self, other):
#         if Water().name + Air().name:
#             return self.name



# water = Element('Земля')
# air = Element('Вода')


Elements = ['Воздух', 'Вода', 'Земля', "Огонь", "Сила"]

for i in Elements:
    for j in Elements:
        if i != j:
            print(Element(i), '+', Element(j), '=', Element(i) + Element(j))

# print(water, '+', air, '=', water + air)

# print(Water(), '+', Air(), '=', Air() + Water())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
