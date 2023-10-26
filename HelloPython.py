#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# First Line
print('Hello Python.')

# sum from 1 to 100
sum_a = 0
count = 1
while count < 101:
    sum_a = sum_a + count
    count = count + 1
print(sum_a)

# 9*9 form
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}x{}={}\t'.format(i, j, i * j), end='')
    print('')


# function
def sum_b(num1, num2):
    return num1 + num2


print(sum_b(100, 200))

# lambda
sum_b = lambda sum1, sum2: sum1 + sum2
print(sum_b(1, 2))

for char in 'liangdianshui':
    print(char, end=' ')

print('\n')

dict1 = {'name': 'zhangsan', 'age': '40', 'sex': 'male'}
for key in dict1:
    print(key, end=' ')

print('\n')

for value in dict1.values():
    print(value, end=' ')

print('\n')


