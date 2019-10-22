# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n):
        self.n = n + 1
        self.i = 0
        self.prime_numbers = []
        self.prime = 0

    def __iter__(self):
        self.i = 1
        self.prime = 0
        return self

    def __next__(self):
        while self.i < self.n:
            self.i += 1
            for j in self.prime_numbers:
                if self.i % j == 0:
                    break
            else:
                self.prime_numbers.append(self.i)
                return self.i
        else:
            raise StopIteration


prime_number_iterator = PrimeNumbers(n=10000)
for number in prime_number_iterator:
    print(number)
print(type(prime_number_iterator))

print(prime_number_iterator.prime_numbers)

print(get_prime_numbers(10000))

print(prime_number_iterator.prime_numbers)


# TODO после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    i = 2
    while i < n:
        prime = True
        for a in range(2, i):
            if i % a == 0:
                prime = False
                break
        if prime:
            yield i
        i += 1

for number in prime_numbers_generator(n=10000):
    if number == 13:
        break
    print(number)

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
def lucky_number(x):
    x = str(x)
    if len(x) % 2 == 0:
        length = len(x)
        half_int_length = int(length / 2)
        start_length = x[:half_int_length]
        end_length = x[-half_int_length:]
        start_sum = sum_number(start_length)
        end_sum = sum_number(end_length)
        print(f'Равность чисел {start_length} и {end_length} = {start_sum==end_sum}, потому что сумма {start_length}'
              f'= {start_sum}, а сумма {end_length} = {end_sum}')

        return True if start_sum == end_sum else False
    else:
        length = len(x)
        half_int_length = int(length / 2)
        start_length = x[:half_int_length]
        end_length = x[-half_int_length:]
        start_sum = sum_number(start_length)
        end_sum = sum_number(end_length)
        print(f'Равность чисел {start_length} и {end_length} = {start_sum==end_sum}, потому что сумма {start_length}'
              f'= {start_sum}, а сумма {end_length} = {end_sum}')
        return True if start_sum == end_sum else False


def sum_number(number):
    sum_number = 0
    for i in str(number):
        sum_number += int(i)
    return sum_number


def palindrome(number):
    number = str(number)
    length = len(number)
    half_int_length = int(length / 2)
    start_length = number[:half_int_length]
    end_length = number[-half_int_length:][::-1]
    print(f'число {int(number)} - полиндром' if start_length == end_length else f'число {int(number)} - не полиндром')
    return True if start_length == end_length else False

def prime_numbers_generator(n):
    i = 2
    while i < n:
        prime = True
        for a in range(2, i):
            if i % a == 0:
                prime = False
                break
        if prime:
            yield i
        i += 1

for number in prime_numbers_generator(n=10000):
    if number == 13:
        break
    print(number)

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


print(prime_factors(525))

# newlist = [345098, 987239, 129872, 7895987, 826412864]
#
# print(lucky_number(12345954123))
#
# print(palindrome(6549456))
#
# print(list(filter(palindrome, newlist)))
#
# print(list(filter(lucky_number, newlist)))