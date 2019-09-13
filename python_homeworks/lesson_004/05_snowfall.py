# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 200


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


# snowflake = sd.snowflake(point, length=length, color=sd.COLOR_WHITE, factor_a=0.6, factor_b=0.35, factor_c=60)
x = 300
y = 450


while True:
    sd.clear_screen()
    point = sd.get_point(x=sd.random_point().x, y=sd.random_point().y)
    for _ in range(N):
        length = sd.random_number(10, 100)
        # sd.snowflake(point, length=length, color=sd.COLOR_WHITE, factor_a=0.6, factor_b=0.35, factor_c=60)
        sd.snowflake(point, length=length, color=sd.COLOR_WHITE, factor_a=0.6, factor_b=0.35, factor_c=60)
        y -= 10
        x += 10

    pass
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


