# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#質數算法3
from math import sqrt
num = int(input('Please enter a number: '))
j = 2
while j <= int(sqrt(num)):
    if num % j == 0:
        print('{:d} is not a prime.'.format(num))
        break
    j += 1
else:
    print('{:d} is a prime.'.format(num))