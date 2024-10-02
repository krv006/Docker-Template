# s = set()
# l = []
# a = ""
# t = (),
# d = {}

# todo collections bir vaqtni ozida bir nechta elementni bir joyda saqlagani yordam beradi
# from collections import namedtuple
#
# Car = namedtuple('Car', ['brand', 'model'])
# car1 = Car(brand="Chevrolet", model="Malibu")
# print(car1.model)  # Natija: Chevrolet


# todo itertools bu takroriy amallardi bajarishda yordam beradi
# from itertools import count
#
# for i in count(10):  # 10 dan boshlanadi
#     if i > 15:
#         break
#     print(i)


# from itertools import accumulate
# numbers = [1, 2, 3, 4]
# for total in accumulate(numbers):
#     print(total)

# todo os bu qaysi operatsion tizimda dastur ishlayotganini aniqlab beradi
# import os
# print(os.name)  # 'posix' (Linux yoki Mac), 'nt' (Windows)

# todo comprehension sodda usl da yozish
# squares = [x**2 for x in range(1, 11)]
# print(squares)
# squares_even = [x**2 for x in range(1, 11) if x % 2 == 0]
# print(squares_even)

# todo lambda qisqa anonim funksiya yaratish
# kvadrat = lambda x: x ** 2
# print(kvadrat(5))  # Natija: 25


# todo Dataclasses oddi class lardi osonlarshtiruvchi vosita

# from dataclasses import dataclass
#
#
# @dataclass
# class Odam:
#     ism: str
#     yosh: int
#     kasb: str
#
#
# odam1 = Odam(ism="Ali", yosh=30, kasb="Dasturchi")
# print(odam1)


# todo OOP principles  asosiy tushunchalari bo‘lib, ular orqali katta va murakkab dasturlarni tuzish, ularni boshqarish va rivojlantirish ancha osonlashadi. OOP dasturlashda hamma narsa ob'ektlar va sinflar asosida quriladi.

# class Hayvon:
#     def ovoz(self):
#         print("Hayvonning ovozi bor")
#
#
# class It(Hayvon):
#     def ovoz(self):
#         print("It vovlaydi")
#
#
# it = Hayvon()
# it.ovoz()  # Natija: It vovlaydi


# using bn join di farqi
# using ikta table da bor narsani ulaydi
# joinga bolsa esa farqi yoq


# class MyClass:
#     __slots__ = ['name', 'age']
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# # MyClass ob'ekti yaratish
# obj = MyClass('Ali', 30)
#
# print(obj.name)  # Ali
# print(obj.age)   # 30

# bookstore/
# │
# ├── docker-compose.yml
# ├── Dockerfile
# ├── app/
# │   ├── main.py
# │   ├── db.py
# │   ├── models.py
# │   └── requirements.txt

