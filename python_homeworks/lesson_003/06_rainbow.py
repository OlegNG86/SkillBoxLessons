# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
point_a = (50, 50)
point_b = (350, 450)
substract_points = []
substract_points.append([[(point_b[0] - point_a[0]) / 2], [(point_b[1] - point_a[1]) / 2]])
point_axis_x = substract_points[0][0][0]
point_axis_y = substract_points[0][1][0]
point_center_circle = sd.get_point(point_axis_x, point_axis_y)
print(point_center_circle)
radius = 150
for i in range(len(rainbow_colors)):
    radius += 5
    sd.circle(point_center_circle, radius=radius, color=(rainbow_colors[i]), width=4)

point_X = sd.get_point(50, 50)
point_Y = sd.get_point(350, 450)
sd.circle(point_X, radius=50, color=rainbow_colors[2], width=5)
sd.circle(point_Y, radius=50, color=rainbow_colors[2], width=5)
sd.circle(point_center_circle, radius=50, color=rainbow_colors[2], width=5)





# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

sd.pause()
