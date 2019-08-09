# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 13:39:30 2019

@author: 10539
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1: return 1
        elif n==2:return 2
        else:
            i=1;j=2
            while n>2:
                j,i=i+j,j
                n-=1
        return j
        