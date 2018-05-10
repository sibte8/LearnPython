# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:43:03 2018

@author: DesktopPC
"""


while True:
    try:
        quantity = int(input("請輸入數量: "))
        price = float(input("請輸入單價: "))
        Cost = quantity * price
        print("總價格是", Cost)
        break
    except ValueError:
        print('請輸入正確的數值')