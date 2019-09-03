# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (800, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# def bubble(point, step):
#     radius = 50
#
#     for _ in range(0, 31, 10):
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2)
#
# point = sd.get_point(100, 100)
# bubble(point=point, step=10)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# def bubble(point, step):
#     radius = 50
#     for _ in range(0, 31, 10):
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2)
#
# point = sd.get_point(100, 100)
# bubble(point=point, step=10)

# Нарисовать 10 пузырьков в ряд
# def bubble(point, step):
#     radius = 25
#     sd.circle(center_position=point, radius=radius, width=2)
#
# for i in range(200, 700, 50):
#     point = sd.get_point(i, 300)
#     bubble(point=point, step=10)

# Нарисовать три ряда по 10 пузырьков
# def bubble(point, step):
#     radius = 25
#     sd.circle(center_position=point, radius=radius, width=2)
#
# for j in range(200, 500, 100):
#     for i in range(200, 700, 50):
#         point = sd.get_point(i, j)
#         bubble(point=point, step=10)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
radius = 20

for _ in range(101):
    point = sd.random_point()
    color = sd.random_color()
    sd.circle(center_position=point, radius=radius, width=2, color=color)

sd.pause()


