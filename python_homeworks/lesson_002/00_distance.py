#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}



print(distances)

M1 = sites['Moscow'][0]
M2 = sites['Moscow'][1]
L1 = sites['London'][0]
L2 = sites['London'][1]
P1 = sites['Paris'][0]
P2 = sites['Paris'][1]

Moscow_London = ((M1 - L1) ** 2 + (M2 - L2) ** 2) ** .5
Moscow_Paris = ((M1 - P1) ** 2 + (M2 - P2) ** 2) ** .5
London_Paris = ((L1 - P1) ** 2 + (L2 - P2) ** 2) ** .5


distances['Moscow_London'] = Moscow_London
distances['Moscow_Paris'] = Moscow_Paris
distances['London_Paris'] = London_Paris

if 'Moscow_London' in distances: print(distances)
print(id(distances['Moscow_Paris']))
print(id(True))
print(id(False))