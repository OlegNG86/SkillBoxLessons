# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def draw_triangle(x=0, y=0, angle=0, length=200):
    point = sd.get_point(x, y)

    v1 = sd.get_vector(point, angle=angle, length=length)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=v1.angle+120, length=v1.length)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=v2.angle+120, length=v2.length)
    v3.draw()


draw_triangle(300, 200, 90, 300)

def draw_rectangle(x=0, y=0, angle=0, length=200):
    point = sd.get_point(x, y)

    v1 = sd.get_vector(point, angle=angle, length=length)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=v1.angle + 90, length=v1.length)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=v2.angle + 90, length=v2.length)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=v3.angle + 90, length=v3.length)
    v4.draw()


# draw_rectangle(250, 150, 35, 300)

def draw_pentagon(x=0, y=0, angle=0, length=200):
    point = sd.get_point(x, y)

    v1 = sd.get_vector(point, angle=angle, length=length)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=v1.angle + 72, length=v1.length)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=v2.angle + 72, length=v2.length)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=v3.angle + 72, length=v3.length)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=v4.angle + 72, length=v4.length)
    v5.draw()


# draw_pentagon(150, 150, 45, 100)

def draw_hexagon(x=0, y=0, angle=0, length=200):
    import simple_draw as sd
    point = sd.get_point(x, y)

    v1 = sd.get_vector(point, angle=angle, length=length)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=v1.angle + 60, length=v1.length)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=v2.angle + 60, length=v2.length)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=v3.angle + 60, length=v3.length)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=v4.angle + 60, length=v4.length)
    v5.draw()

    v6 = sd.get_vector(start_point=v5.end_point, angle=v5.angle + 60, length=v5.length)
    v6.draw()

    sd.pause()

def draw_multy(object=3, x=0, y=0, angle=0, length=200):
    point = sd.get_point(x, y)

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

        v1 = sd.get_vector(point, angle=angle, length=length)
        v1.draw()

        v2 = sd.get_vector(start_point=v1.end_point, angle=v1.angle + anglePlus, length=v1.length)
        v2.draw()

        v3 = sd.get_vector(start_point=v2.end_point, angle=v2.angle + anglePlus, length=v2.length)
        v3.draw()

        if object >=4:

            v4 = sd.get_vector(start_point=v3.end_point, angle=v3.angle + anglePlus, length=v3.length)
            v4.draw()

            if object >=5:

                v5 = sd.get_vector(start_point=v4.end_point, angle=v4.angle + anglePlus, length=v4.length)
                v5.draw()

                if object >=6:

                    v6 = sd.get_vector(start_point=v5.end_point, angle=v5.angle + anglePlus, length=v5.length)
                    v6.draw()

sd.pause()

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()