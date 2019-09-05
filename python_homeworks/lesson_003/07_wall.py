# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
for i in range(50, 400, 55):
    X_left = 100
    Y_left = 100+i
    X_right = 200
    Y_right = 150+i
    point_left_bottom = sd.get_point(X_left, Y_left)
    point_right_top = sd.get_point(X_right, Y_right)
    sd.rectangle(left_bottom=point_left_bottom, right_top=point_right_top)
    for j in range(100, 500, 105):
        point_left_bottom = sd.get_point(X_left+5+j, Y_left)
        point_right_top = sd.get_point(X_right+5+j, Y_right)
        sd.rectangle(left_bottom=point_left_bottom, right_top=point_right_top)



sd.pause()
