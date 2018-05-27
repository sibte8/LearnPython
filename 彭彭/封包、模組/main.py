# -*- coding: utf-8 -*-
"""
Created on Tue May 15 22:12:15 2018

@author: DesktopPC
"""

import sys
sys.path.append('D:\Github\LearnPython')

import geometry.point
result=geometry.point.distance(3,4)
print(result)

import geometry.line as line
result=line.slope(1,1,3,3)
print('slope',result)