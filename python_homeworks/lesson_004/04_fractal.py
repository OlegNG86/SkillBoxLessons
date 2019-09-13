# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

def draw_branches(start_point, angle_draw, lenght_branches, count=10):
    if count == 0:
        return

    if lenght_branches < 1:
        return
    else:
        v1 = sd.get_vector(start_point, angle_draw + 30, length=lenght_branches)
        v1.draw()
        v2 = sd.get_vector(start_point, angle_draw - 30, length=lenght_branches)
        v2.draw()
        count -= 1
        next_length = v1.length * (.75 * (sd.random_number(80, 100)/100))
        next_angle1 = v1.angle + 30 * sd.random_number(60, 100) / 100
        next_angle2 = v2.angle - 30 * sd.random_number(60, 100) / 100
        draw_branches(start_point=v1.end_point, angle_draw=next_angle1, lenght_branches=next_length, count=count)
        draw_branches(start_point=v2.end_point, angle_draw=next_angle2, lenght_branches=next_length, count=count)


root_point = sd.get_point(300, 30)
draw_branches(start_point=root_point, angle_draw=90, lenght_branches=100)



# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


