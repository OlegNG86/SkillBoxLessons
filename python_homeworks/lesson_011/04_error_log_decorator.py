# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'
import os


def log_errors(decor_name):
    def decorator(func):
        def surrogate(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as exc:
                filepath = decor_name
                func_name = func.__name__
                func_param = func.__code__.co_varnames
                type_error = type(exc)
                text_error = exc.__str__()
                output = f'Имя функции: {func_name}, параметры вызова: {func_param}, ' \
                         f'тип ошибки: {type_error}, текст ошибки: {text_error}\n'
                if os.path.exists(filepath):
                    with open(filepath, 'a', encoding='utf-8') as f:
                        f.write(output)
                else:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(output)
                return None

        return surrogate

    return decorator


# Проверить работу на следующих функциях
@log_errors('function_errors.log')
def perky(param):
    return param / 0


@log_errors('function_errors.log')
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')
perky(param=42)

# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass
