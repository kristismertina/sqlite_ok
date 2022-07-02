'''
1. Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации
(отвечающий за добавку к выбираемому лимонаду).
В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия
добавки, а иначе отобразится следующая фраза: «Обычная газировка».

'''


class Soda:

    def __init__(self, ingr):
        self.ingr = ingr

    def have(self):
        if self.ingr == 'orange':
            return self.show_my_drink()
        elif self.ingr == 'banana':
            return self.show_my_drink()
        else:
            print('Обычная газировка')

    def show_my_drink(self):
        return f'Газировка с добакой {self.ingr}'


new_soda = Soda('banana')
print(new_soda.have())

'''

2. Николай – оригинальный человек.
Он решил создать класс Nikola, принимающий при инициализации 2 параметра: имя и возраст. Но на этом
он не успокоился.
Не важно, какое имя передаст пользователь при создании экземпляра, оно всегда будет содержать “Николая”.
В частности - если пользователя на самом деле зовут Николаем, то с именем ничего не произойдет, а если
его зовут, например, Максим, то оно преобразуется в “Я не Максим, а Николай”.
Более того, никаких других атрибутов и методов у экземпляра не может быть добавлено, даже если кто-то и
 вздумает так поступить (т.е. если некий пользователь решит прибавить к экземпляру свойство «отчество»
 или метод «приветствие», то ничего у такого хитреца не получится).
Для ограничения количества наборов свойств и методов в экземпляре применяется специальный магический
атрибут __slots__.
'''


class Nikola:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def new_exemp(self):
        if self.name != 'Nikola':
            return self.i_am_nikola()
        else:
            print('Верно, я Николай')

    def i_am_nikola(self):
        return f'Я не {self.name} Я Николай!'


exem = Nikola('Nfff', 23)
print(exem.new_exemp())

'''
3. Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age.
 По умолчанию name = Ivan, age = 18, groupNumber = 10A. Необходимо создать пять методов: getName,
 getAge, getGroupNumber, setNameAge, setGroupNumber. Метод getName нужен для получения данных об имени
  конкретного студента, метод getAge нужен для
получения данных о возрасте конкретного студента, vетод setGroupNumberнужен для получения данных
о номере группы конкретного студента. Метод SetNameAge позволяет изменить данные атрибутов установленных
 по умолчанию, метод setGroupNumber позволяет изменить номер группы установленный по умолчанию.
  В программе необходимо создать пять
экземпляров класса Student, установить им разные имена, возраст и номер группы.

'''


class Student:

    def __init__(self, name='Ivan', age=18, groupNumber='10a'):
        self._name = name
        self._age = age
        self._groupNumber = groupNumber

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def getGroupNumber(self):
        return self._groupNumber

    def setNameAge(self, x, y):
        self._name = x
        self._age = y
        return f'{self._name}, {self._age}'

    def setGroupNumber(self, a):
        self._groupNumber = a
        return f'{self._groupNumber}'


obj = Student()
print(obj._name)
print(obj.getName())
print(obj.getAge())
print(obj.getGroupNumber())
print(obj.setNameAge('sasha', 12))
print(obj.setGroupNumber(234))
'''
4. Напишите программу с классом Math. Создайте два атрибута — a и b. Напишите методы addition
— сложение, multiplication — умножение, division — деление, subtraction — вычитание. При
передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.
'''

import math


class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a}, {self.b}'

    def addition(self):
        return self.a + self.b

    def division(self):
        try:
            if self.b and self.a != 0:
                if self.a > self.b:
                    return self.a / self.b
        except ZeroDivisionError:
            print('на 0 делить нельзя')

    def multiplication(self):
        return self.a * self.b

    def subtraction(self):
        return self.a - self.b

    @staticmethod
    def fact(x):
        return math.factorial(x)


obj1 = Math(2, 1)
print(obj1.b)
print(obj1.multiplication())
print(obj1.division())
'''
5.Напишите программу с классом Car. Создайте конструктор класса Car. Создайте атрибуты класса
Car — color (цвет), type (тип), year (год). Напишите пять методов. Первый — запуск автомобиля,
при его вызове выводится сообщение «Автомобиль заведен». Второй — отключение автомобиля — выводит
 сообщение «Автомобиль заглушен». Третий — присвоение автомобилю года выпуска. Четвертый метод — присвоение
 автомобилю типа. Пятый — присвоение автомобилю цвета.

'''

class Car():

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year


    def go(self):
        return f'Автомобиль заведен'

    def finish(self):
        return f'Автомобиль заглушен'

    def year_car(self, a):
        self.year = a
        return f'Год выпуска авто: {self.year}'

    def type_car(self, d):
        self.type = d
        return f' Марка авто: {self.type}'

    def color_car(self, w):
        self.color = w
        return f'Цвет авто: {self.color}'


car = Car('black', 'bmw', 2020)
print(car.go())
print(car.type_car('volvo'))
print(car.year_car(2012))