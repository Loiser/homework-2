# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 02:59:23 2019

@author: 10539
"""

def suum(x):
    if x==1 or x==2 :
        return 1
    else:
        return (suum(x-1)+suum(x-2))
    
print(suum(6))