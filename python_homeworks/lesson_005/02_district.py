# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join


from district.central_street.house1 import room1 as cent1room, room2 as cent2room
from district.central_street.house2 import room1 as r1, room2 as r2

from district.soviet_street.house1 import room1 as sh1r1, room2 as sh1r2
from district.soviet_street.house2 import room1 as sh2r1, room2 as sh2r2

# from district.soviet_street.house1 import room1.folks as rf

print('На Центральной улице живут: ')

print(', '.join(cent1room.folks + cent2room.folks + r1.folks + r2.folks))


print('\nНа Советской улице живут: ')
print(', '.join(sh1r1.folks + sh1r2.folks + sh2r1.folks + sh2r2.folks))
