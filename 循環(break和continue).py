# -*- coding: utf-8 -*-
"""
Created on Tue May  8 16:48:42 2018

@author: DesktopPC
"""


print('例子：循環中的break')
sumA = 0
i = 1
while i <= 5:
    sumA += i
    if i == 3:
        break
    print('i={},sum={}'.format(i,sumA))
    i += 1

print('例子：循環中的continue')
sumA = 0
i = 1
while i <= 5:
    sumA += i
    i += 1
    if i == 3:
        continue
    print('i={},sum={}'.format(i,sumA))