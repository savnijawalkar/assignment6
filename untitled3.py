# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 14:14:59 2022

@author: Dell
"""

#3


def pascal_triangle(n):
   row = [1]
   y = [0]
   for x in range(max(n,0)):
      print(row)
      row=[l+r for l,r in zip(row+y, y+row)]
   return n>=1
pascal_triangle(6)