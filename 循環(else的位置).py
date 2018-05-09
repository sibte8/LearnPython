# -*- coding: utf-8 -*-
"""
Created on Tue May  8 22:34:09 2018

@author: DesktopPC
"""

print('else 放的位置1')
for i in range(1, 10, 2):
    if i % 5 == 0:
        print("Bingo!")
        break
else:
    print(i)


print('else 放的位置2')
for i in range(1, 10, 2):
    if i % 5 == 0:
        print("Bingo!")
        break
    else:
        print(i)