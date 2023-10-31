#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum, unique

Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
Enum('Weekday', ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fir', 'Sat'))
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fir = 5
    Sat = 6

@unique
class Month(Enum):
    Jan = 'Janurary'
    Feb = 'February'
    Mar = 'March'
    Apr = 'April'
    May = 'May'
    Jun = 'June'
    Jul = 'July'
    Aug = 'August'
    Sep = 'September'
    Oct = 'October'
    Nov = 'November'
    Dec = 'December'


if __name__ == '__main__':
    print(Weekday.Sun, '---', Weekday.Sun.name, '---', Weekday.Sun.value)
    for(name, member) in Month.__members__.items():
        print(name, '---', member, '---', member.value)
    for(name, member) in Weekday.__members__.items():
        print(name, '---', member, '---', member.value)
