# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def draw_multy(object=3, x=0, y=0, angle=0, length=200):

    point = sd.get_point(x, y)
    shapes = {1: 'Треугольник',
             2: 'Квадрат',
             3: 'Пятиугольник',
             4: 'Шестиугольник'}

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
    k = int(input())
    while k not in colors:
        try:
            value1 = input()
            print('Вы ввели некорректный номер')
            if int(value1) in colors:
                k = value1
            else:
                continue
        except:
            print('Вы ничего не ввели')

    color = colors.get(int(k))[0]

    for k, v in shapes.items():
        print(k, v)
    print('Выберите фигуру: ')

    s = int(input())
    while s not in shapes:
        try:
            value1 = input()
            print('Вы ввели некорректный номер')
            if int(value1) in shapes:
                s = value1
            else:
                continue
        except:
            print('Вы ничего не ввели')


    shape = int(s)
    object = shape + 2

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

draw_multy(3, 250, 240, angle=45, length=200)


sd.pause()
