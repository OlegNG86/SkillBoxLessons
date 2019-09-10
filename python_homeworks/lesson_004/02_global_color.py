# -*- coding: utf-8 -*-
from pprint import pprint

import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

def draw_multy(object=3, x=0, y=0, angle=0, length=200):

    point = sd.get_point(x, y)
    colors = {1: [(sd.COLOR_RED), 'Красный'],
             2: [(sd.COLOR_ORANGE), 'Оранжевый'],
             3: [(sd.COLOR_YELLOW), 'Жёлтый'],
             4: [(sd.COLOR_GREEN), 'Зелёный'],
             5: [(sd.COLOR_CYAN), 'Синий'],
             6: [(sd.COLOR_BLUE), 'Голубой'],
             7: [(sd.COLOR_PURPLE), 'Фиолетовый']}

    for k, v in colors.items():
        print(k, v[1])
    print('Выберите цвет: ')
    k = input()
    color = colors.get(int(k))[0]

    if object < 0:
        print('Вы задали слишком мало точек.')

    if object == 3:
        anglePlus = 120
    elif object == 4:
        anglePlus = 90
    elif object == 5:
        anglePlus = 72
    else:
        anglePlus = 60


    if object >= 3:

        v1 = sd.get_vector(point, angle=angle, length=length, )
        v1.draw(color=color)

        v2 = sd.get_vector(start_point=v1.end_point, angle=v1.angle + anglePlus, length=v1.length)
        v2.draw(color=color)

        v3 = sd.get_vector(start_point=v2.end_point, angle=v2.angle + anglePlus, length=v2.length)
        v3.draw(color=color)

        if object >=4:

            v4 = sd.get_vector(start_point=v3.end_point, angle=v3.angle + anglePlus, length=v3.length)
            v4.draw(color=color)

            if object >=5:

                v5 = sd.get_vector(start_point=v4.end_point, angle=v4.angle + anglePlus, length=v4.length)
                v5.draw(color=color)

                if object >=6:

                    v6 = sd.get_vector(start_point=v5.end_point, angle=v5.angle + anglePlus, length=v5.length)
                    v6.draw(color=color)

draw_multy(3, 300, 150, angle=45, length=200)

sd.pause()
