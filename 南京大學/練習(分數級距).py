# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:00:38 2018

@author: DesktopPC
"""

#判斷分數級距
score = eval(input("請輸入分數: "))
if  0 <= score <= 100:
    if 90 <= score <= 100:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 0:
        grade = "D"
    print("分數 {} 的級距是 {}.".format(score, grade))
else:
    print("請輸入0~100的分數")