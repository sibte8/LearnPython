# -*- coding: utf-8 -*-
"""
Created on Wed May  9 18:48:33 2018

@author: DesktopPC
"""


def hanoi(a,b,c,n):
    if n==1:
        print(a,'->',c)
    else:
        hanoi(a,c,b,n-1)
        print(a,'->', c)
        hanoi(b,a,c,n-1)
hanoi('a','b','c',4)
