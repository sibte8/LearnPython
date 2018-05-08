# -*- coding: utf-8 -*-
"""
Created on Tue May  8 15:03:02 2018

@author: DesktopPC
"""


#生成0~9的整數序列
[i for i in range(10)] 


#生成0~10裡的奇數序列
[i+1 for i in range(10) if i%2==0]
[i for i in range(10) if i%2==1]
   
#生成0~10裡的偶數序列
[i for i in range(10) if i%2==0]

#生成器表達式
(i+1 for i in range(10) if i%2==0)