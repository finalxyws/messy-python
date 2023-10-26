#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# create a list from 1 to 100, and print all the prime number
list_a = []
for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        list_a.append(i)
print(list_a)