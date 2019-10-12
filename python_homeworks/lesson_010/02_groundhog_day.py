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


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


ENLIGHTENMENT_CARMA_LEVEL = 777


def one_day():
    with open('log_of_exceptions.txt', 'w') as text_file:
        text_file.write('')
    CARMA_LEVEL = 0
    log_exception_cacher = []
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
        try:
            if rand_choice == 1:
                rand_exception = choice(exceptions)
                log_exception_cacher.append(rand_exception)
                with open('log_of_exceptions.txt', 'a') as text_file:
                    text_file.write(rand_exception + '\n')
                if rand_exception == 'IamGodError':
                    raise IamGodError('Режим бога')
                if rand_exception == 'DrunkError':
                    raise DrunkError('Пьяный')
                if rand_exception == 'CarCrashError':
                    raise CarCrashError('Разбитая машина')
                if rand_exception == 'GluttonyError':
                    raise GluttonyError('Обжора')
                if rand_exception == 'DepressionError':
                    raise DepressionError('Дипрессия')
                if rand_exception == 'SuicideError':
                    raise SuicideError('Самоубийца')
        except IamGodError as exc:
            print(f'поймана ошибка {exc}!')
        except DrunkError as exc:
            print(f'поймана ошибка {exc}!')
        except CarCrashError as exc:
            print(f'поймана ошибка {exc}!')
        except GluttonyError as exc:
            print(f'поймана ошибка {exc}!')
        except DepressionError as exc:
            print(f'поймана ошибка {exc}!')
        except SuicideError as exc:
            print(f'поймана ошибка {exc}!')

    print(f'Уровень кармы {CARMA_LEVEL}, пойманных исключений {len(log_exception_cacher)}, '
          f'а именно {log_exception_cacher}')


one_day()

# https://goo.gl/JnsDqu
