# -*- coding: utf-8 -*-
"""
Created on Tue May  8 14:37:55 2018

@author: DesktopPC
"""

from random import randint
x = randint(0, 300)
for count in range(0,5): #執行5次
    digit = int(input('Please input a number between 0~300: '))
    if digit == x :
        print('Bingo!')
    elif digit > x:
        print('Too large, please try again.')
    else:
        print('Too small, please try again.')
