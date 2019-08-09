# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 02:01:09 2019

@author: 10539
"""

def ispair(x,y) -> bool:
    if x=='{' :
        if y!='}':
            return 0
        else:
            return 1
    elif x=='(' :
        if y!=')':
            return 0
        else:
            return 1
    elif x=='[' :
        if y!=']':
            return 0
        else:
            return 1

class Solution():
        
    def isValid(self, s: str) -> bool:
        lis=[]
        for i in range(len(s)):
            if s[i]=='{'or s[i]=='[' or s[i]=='(':
                lis.append(s[i])
            else:
                if len(lis)==0:
                    return False
                else:
                    if ispair(lis[len(lis)-1],s[i])==1:
                        lis.pop()
                    else:
                        return False
        return len(lis)==0                    
ll=Solution()          
print(ll.isValid('{[]}'))