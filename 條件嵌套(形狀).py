# -*- coding: utf-8 -*-
"""
Created on Tue May  8 11:09:21 2018

@author: DesktopPC
"""

# Filename: ifnestpro.py
k = input('input the index of shape: ')
if k == '1':
    print('5circle')
elif k == '2':
    print('oval')
elif k == '3':
    sd1 = int(input('the first side: '))
    sd2 = int(input('the second side : '))
    if sd1 == sd2:
        print("the square's area is", sd1*sd2)
    else:
        print("the rectangle's area is", sd1*sd2)
elif k == '4':
    print('triangle')
else:
    print('you input the invalid number')