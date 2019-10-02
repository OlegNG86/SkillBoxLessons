# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 100
        self.mud = 0
        self.coat = 0
        self.food_for_cat = 30

    def __str__(self):
        return 'В доме денег {}, еды {}, грязи {}, шуб {}'.format(self.money, self.food, self.mud, self.coat)


class Citizen:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.happiness = 100
        self.house = home

    def __str__(self):
        return 'Я - {}, я сыт на {}, я счастлив на {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        if self.house.food >= 30:
            self.house.food -= 30
            self.fullness += 30
            self.happiness += 10
            return cprint('{} поел(а)!'.format(self.name), color='green')
        else:
            return

    def pet_cat(self):
        self.happiness += 10
        cprint('{} гладит кота!'.format(self.name), color='green')
        self.fullness -= 10


class Husband(Citizen):

    def __init__(self, name):
        super().__init__(name)

    def act(self):
        if self.fullness <= 0:
            return cprint('{} умер(ла)...'.format(self.name), color='red')
        if self.happiness < 10:
            return cprint('{} умер(ла) от депрессии...'.format(self.name), color='red')
        home.mud += 5
        dice = randint(1, 6)
        if home.mud > 90:
            self.happiness -= 10
        if self.fullness <= 20:
            self.eat()
        elif self.happiness <= 20:
            self.gaming()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.gaming()
        else:
            self.pet_cat()

    def work(self):
        cprint('{} сходил на работу!'.format(self.name), color='green')
        home.money += 400
        self.fullness -= 10

    def gaming(self):
        cprint('{} поиграл в WoT!'.format(self.name), color='green')
        self.fullness -= 10
        self.happiness += 20


class Wife(Citizen):

    def __init__(self, name):
        super().__init__(name)

    def act(self):
        if self.fullness <= 0:
            return cprint('{} умер(ла)...'.format(self.name), color='red')
        if self.happiness < 10:
            return cprint('{} умер(ла) от депрессии...'.format(self.name), color='red')
        dice = randint(1, 6)
        if home.mud > 90:
            self.happiness -= 10
        if self.fullness <= 20:
            self.eat()
        elif self.house.food <= 100:
            self.shopping()
        elif self.happiness <= 20:
            self.buy_fur_coat()
        elif self.house.mud >= 100:
            self.clean_house()
        elif dice == 1:
            self.shopping()
        elif dice == 2:
            self.buy_fur_coat()
        else:
            self.pet_cat()

    def shopping(self):
        if self.house.money >= 10:
            cprint('{} сходила в магазин!'.format(self.name), color='green')
            self.house.money -= 50
            self.house.food += 50
            self.fullness -= 10
        else:
            return

    def buy_fur_coat(self):
        if self.house.money >= 350:
            self.house.money -= 350
            self.house.coat += 1
            self.happiness += 60
            self.fullness -= 10
            cprint('{} купила шубу!!!'.format(self.name), color='green')
        else:
            return

    def clean_house(self):
        self.house.mud -= 100
        cprint('{} убралась дома!'.format(self.name), color='green')


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(home, color='cyan')


# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30

    def __str__(self):
        if self.fullness <= 0:
            return '{} умер от голода...'.format(self.name)

        else:
            return 'Я - {}, я сыт на {}'.format(self.name, self.fullness)

    def act(self):
        if self.fullness <= 20:
            self.eat()
        dice = randint(1, 6)
        if dice == 1:
            self.soil()
        else:
            self.sleep()

    def eat(self):
        if home.food_for_cat >= 10:
            cprint('{} кот ест!'.format(self.name), color='green')
            home.food_for_cat -= 10
            self.fullness += 20

    def sleep(self):
        cprint('{} кот спит!'.format(self.name), color='green')

    def soil(self):
        cprint('{} кот дерёт обои!'.format(self.name), color='green')
        home.mud += 5


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Husband, Wife):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness <= 20:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        super().act()

    def sleep(self):
        cprint('{} спит!'.format(self.name), color='green')


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')
anfis = Cat(name='Анфис')
kotka = Cat(name='Котька')
kosha = Cat(name='Коша')
markiz = Cat(name='Маркиз')

for day in range(366):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    anfis.act()
    kotka.act()
    kosha.act()
    markiz.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')
    cprint(anfis, color='cyan')
    cprint(kotka, color='cyan')
    cprint(kosha, color='cyan')
    cprint(markiz, color='cyan')
    cprint(home, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
