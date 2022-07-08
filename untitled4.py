# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 14:16:56 2022

@author: Dell
"""

 #4


import string, sys
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())
 
print ( ispangram('The quick brown fox jumps over the lazy dog'))