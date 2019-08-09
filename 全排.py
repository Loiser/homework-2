# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 03:12:53 2019

@author: 10539
"""
#回溯二叉树
def perm(lis,begin,end):
    if begin>=end:
        print(lis)
    else:
        i = begin 
        for num in range(begin,end):
            lis[num],lis[i] = lis[i],lis[num]
            perm(lis,begin+1,end)
            lis[num],lis[i] = lis[i],lis[num]

lis = [1,2,3,4,5]
perm(lis,0,len(lis))