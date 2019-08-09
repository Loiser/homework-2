# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 02:29:12 2019

@author: 10539
"""

class Solution:
    def evalRPN(self, tokens) -> int:
        f1 = lambda a,b:a+b
        f2 = lambda a,b:a-b
        f3 = lambda a,b:a*b
        f4 = lambda a,b:int(a/b)
        maps = {'+':f1,'-':f2,'*':f3,'/':f4}
        stack = []
        for i in tokens:
            if i in maps:
                a = stack.pop()
                b = stack.pop()
                stack.append(maps[i](b,a))
            else:
                i = int(i)
                stack.append(i)
        return stack[-1]