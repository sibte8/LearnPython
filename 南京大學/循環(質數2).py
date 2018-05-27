# -*- coding: utf-8 -*-
"""
Created on Tue May  8 15:52:40 2018

@author: DesktopPC
"""


#質數算法2
from math import sqrt
for i in range(2,101):
    flag=1
    k = int(sqrt(i))
    for j in range(2,k+1):
        if i%j==0:
            flag=0
            break
    if(flag):
        print(i, end = ' ')
            