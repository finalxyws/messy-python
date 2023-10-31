#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Meter(object):
    def __init__(self, value=0.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Foot(object):
    def __get__(self, instance, owner):
        return instance.meter * 3.2808

    def __set__(self, instance, value):
        instance.meter = float(value) / 3.2808


class Distance(object):
    meter = Meter()
    foot = Foot()


def distance_converter():
    d = Distance()
    convert_unit = input('Please choose the unit you want to convert: ')
    if convert_unit == 'meter':
        print('Please input the value of meter: ')
        d.meter = input()
        print('The value of meter is: ', d.meter)
        print('The value of foot is: ', d.foot)
    else:
        print('Please input the value of foot: ')
        d.foot = input()
        print('The value of foot is: ', d.foot)
        print('The value of meter is: ', d.meter / 3.2808)


class Pound(object):
    def __init__(self, value=0.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Kilogram(object):
    def __get__(self, instance, owner):
        return instance.pound * 0.453592

    def __set__(self, instance, value):
        instance.pound = float(value) / 0.453592


class Weight(object):
    pound = Pound()
    kilogram = Kilogram()


def weight_converter():
    w = Weight()
    convert_unit = input('Please choose the unit you want to convert: ')
    if convert_unit == 'pound':
        print('Please input the value of pound: ')
        w.pound = input()
        print('The value of pound is: ', w.pound)
        print('The value of kilogram is: ', w.kilogram)
    else:
        print('Please input the value of kilogram: ')
        w.kilogram = input()
        print('The value of kilogram is: ', w.kilogram)
        print('The value of pound is: ', w.pound / 0.453592)
