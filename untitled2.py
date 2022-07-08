# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 14:14:42 2022

@author: Dell
"""

#2


def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
print(isPalindrome('aza'))