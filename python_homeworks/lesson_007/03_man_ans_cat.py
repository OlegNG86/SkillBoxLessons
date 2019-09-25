# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# -*- coding: utf-8 -*-

from random import randint

# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')
            self.shopping()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_mtv(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def cat_shop(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой для кота'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food_for_cat += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def cleaning(self):
        if self.house.mud_from_cat > 100:
            cprint('{} убрался дома'.format(self.name), color='magenta')
            self.fullness -= 20
            self.house.mud_from_cat -= 100
        else:
            cprint('{} уборка не требуется!'.format(self.name), color='red')
            self.work()

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def pick_up_a_cat(self, house, Cat):
        Cat.house = house
        self.fullness -= 10
        Cat.house.food_for_cat = 0
        Cat.house.mud_from_cat = 0
        cprint('{} подобрал кота'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.food_for_cat < 10:
            self.cat_shop()
        elif self.house.money < 100:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.cleaning()
        else:
            self.watch_mtv()


class House:

    def __init__(self):
        self.food = 50
        self.money = 100
        self.food_for_cat = None
        self.mud_from_cat = None

    def __str__(self):
        if self.food_for_cat != None:

            return 'В доме еды осталось {}, денег осталось {}, еды для кота {}, грязи от кота {}'.format(
                self.food, self.money, self.food_for_cat, self.mud_from_cat)
        else:
            return 'В доме еды осталось {}, денег осталось {}'.format(
                self.food, self.money)


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food_for_cat >= 10:
            cprint('{} поел(а)'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.food_for_cat -= 10
        else:
            cprint('{}, нет еды для кота'.format(self.name), color='red')

    def sleep(self):
        cprint('{} поспал'.format(self.name), color='blue')
        self.fullness -= 10

    def play(self):
        cprint('{} дерёт обои'.format(self.name), color='green')
        self.fullness -= 10
        self.house.mud_from_cat += 5

    # def go_to_the_house(self, house):
    #     self.house = house
    #     self.fullness -= 10
    #     self.house.food_for_cat = 0
    #     self.house.mud_from_cat = 0
    #     cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер(ла)...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.play()
        else:
            self.sleep()


little_cat = Cat('Анфиска')

citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]

my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

Man('Бивис').pick_up_a_cat(my_sweet_home, little_cat)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    little_cat.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    print(little_cat)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
