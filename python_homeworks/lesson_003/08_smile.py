# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def draw_smile(x=250, y=250, color=sd.random_color()):
    X_coord = x
    Y_coord = y
    color = sd.random_color()
    radius_circle = 100
    point_center_circle = sd.get_point(X_coord, Y_coord)
    point_left_eye = sd.get_point(int(X_coord - 30), Y_coord + 30)
    point_right_eye = sd.get_point(int(X_coord + 30), Y_coord + 30)
    sd.circle(point_center_circle, radius=radius_circle, width=5, color=color)
    sd.circle(point_left_eye, radius=int(radius_circle/10), width=0)
    sd.circle(point_right_eye, radius=int(radius_circle/10), width=0)
    point1 = sd.get_point(X_coord - 20, Y_coord - 20)
    point2 = sd.get_point(X_coord + 20, Y_coord - 20)
    list1 = [point1, point2]
    sd.lines(list1, width=5)


for _ in range(10):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    draw_smile(x, y)


sd.pause()