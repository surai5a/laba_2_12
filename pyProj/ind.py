#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def deco(func):
    def wrapper(r):
        radius = float(func(r))
        print("Площадь круга равна = ", "%.2f" % radius)
    return wrapper


@deco
def rad(r):
    radius = float(3.14 * (r * r))
    return radius


a = float(input("Введите радиус: "))
rad(a)
