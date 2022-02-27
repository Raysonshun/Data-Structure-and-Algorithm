# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 15:11:36 2022

@author: luxin
"""

def quicksort(s):
    
    if len(s) == 1:
        return s
    pivot = s[0]
    left = [ i for i in s[1:] if i <= pivot]
    right = [ i for i in s[1:] if i >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)