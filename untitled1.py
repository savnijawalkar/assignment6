# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 14:14:15 2022

@author: Dell
"""

#1


def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(6))
 


 