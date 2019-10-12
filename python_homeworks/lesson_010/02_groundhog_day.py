# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

from random import randint
from random import choice

ENLIGHTENMENT_CARMA_LEVEL = 777


def one_day():
    CARMA_LEVEL = 0
    while CARMA_LEVEL < ENLIGHTENMENT_CARMA_LEVEL:
        rand_carma = randint(1, 7)
        CARMA_LEVEL += rand_carma
        exceptions = ['IamGodError',
                      'DrunkError',
                      'CarCrashError',
                      'GluttonyError',
                      'DepressionError',
                      'SuicideError']
        rand_choice = randint(1, 13)
        if rand_choice == 1:
            rand_exception = choice(exceptions)
        else:
            rand_exception = None
    return CARMA_LEVEL, rand_exception


print(one_day())

# https://goo.gl/JnsDqu
