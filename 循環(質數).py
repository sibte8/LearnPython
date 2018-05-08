# -*- coding: utf-8 -*-
"""
Created on Tue May  8 15:27:39 2018

@author: DesktopPC
"""


#質數算法1
from math import sqrt
j = 2
while j <=100:
    #判斷每個數是否為質數(不可被2~根號x整除)
    i = 2
    k= sqrt(j)
    while i <= k:
        if j%i == 0: break #i是j的因子，不是質數了
        i = i+1
    if i > k:
        print(j, end = ' ')
    j += 1