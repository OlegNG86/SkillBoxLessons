# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
point_left_bottom = sd.get_point(100, 100)
point_right_top = sd.get_point(200, 150)


sd.rectangle(left_bottom=point_left_bottom, right_top=point_right_top)


sd.pause()
