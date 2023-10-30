#!/usr/bin/env python3
# coding: utf-8

class Person():
    var_prop = 'test_person'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('{} is eating.'.format(self.name))

    def sleep(self):
        print('{} is sleeping.'.format(self.name))

    def play(self):
        print('{} is playing.'.format(self.name))

    def person_prop(self):
        print('This is a person class. {0}'.format(self.var_prop))

    def change_prop(self):
        self.var_prop = input('Please input a new prop: ')
        print('The new prop is: {0}'.format(self.var_prop))


p1 = Person('zhangsan', 20)
p1.eat()
p1.sleep()
p1.play()