#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# create a list from 1 to 100, and print all the prime number
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def find_prime(num):
    list_a = []
    for i in range(2, num):
        if is_prime(i):
            list_a.append(i)
    print('The prime number list is: ', list_a)
    return list_a
