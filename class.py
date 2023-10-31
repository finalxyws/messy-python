#!/usr/bin/env python3
# coding: utf-8

class Person(object):
    var_prop = 'Human in nature.'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __del__(self):
        print('{0} is deleted.'.format(self.name))

    def print_info(self):
        print('Hello, {0}.'.format(self.name))

    def eat(self):
        print('{} is eating.'.format(self.name))

    def sleep(self):
        print('{} is sleeping.'.format(self.name))

    def play(self):
        print('{} is playing.'.format(self.name))

    def change_prop(self):
        self.var_prop = input('Please input a new prop: ')
        print('The new prop is: {0}'.format(self.var_prop))


class PersonVIP(Person):
    def print_info(self):
        print('Hello, VIP {0}.'.format(self.name))


class PersonGeneral(Person):
    def print_info(self):
        print('Hello, General {0}.'.format(self.name))


p1 = Person('zhang san', 20, 'male')

p1.print_info()
# p1.eat()
# p1.sleep()
# p1.play()

pVIP = PersonVIP('Sheldon', 40, 'male')
pVIP.print_info()

pGeneral = PersonGeneral('Lucy', 30, 'female')
pGeneral.print_info()
