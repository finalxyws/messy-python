#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# def fibonacci_sequence(num):
#     list_a = [0, 1]
#     for i in range(2, num):
#         list_a.append(list_a[i - 1] + list_a[i - 2])
#     print('The fibonacci sequence is: ', list_a)
#     return list_a


# use generator to generate fibonacci sequence and print it
def fibonacci_sequence_generator(num):
    a, b = 0, 1
    for i in range(num):
        yield b
        a, b = b, a + b


for i in fibonacci_sequence_generator(10):
    print(i)
