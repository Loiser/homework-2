# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 03:11:23 2019

@author: 10539
"""

def mul(x):
    if x==1 or x==0 :
        return 1
    else:
        return (x*mul(x-1))
    
print(mul(5))