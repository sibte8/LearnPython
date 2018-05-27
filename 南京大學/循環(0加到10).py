# -*- coding: utf-8 -*-
"""
Created on Tue May  8 14:49:56 2018

@author: DesktopPC
"""

sumA=0
j=1
while j<10:
    sumA+=j
    j+=1
print('j={},sum={}'.format(j, sumA))


#break語句
sumA = 0
i = 1
while True:
    sumA += i
    i += 1
    if sumA > 10:
       break
print('i={},sum={}'.format(i, sumA))