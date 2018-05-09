# -*- coding: utf-8 -*-
"""
Created on Wed May  9 16:10:35 2018

@author: DesktopPC
"""


print('正確解法')
#質數算法4
from math import sqrt
def isprime(x):
    if x == 1:
        return False
    k = int(sqrt(x))
    for j in range(2,k+1):
        if x%j == 0:
            return False
    return True
for i in range(2,101):
    if isprime(i):
        print( i, end = ' ')



print('↓else放在錯誤的地方')
def isprime(x):
    if x == 1:
        return False
    k = int(sqrt(x))
    for j in range(2, k+1):
         if x % j == 0:
             return False
         else:
             return True
for i in range(2,101):
    if isprime(i):
        print( i, end = ' ')
#这样写变成了判断x的奇偶性，
#因为只判断了j是2的情况就得到了“x是素数”的判断结果（False或True）