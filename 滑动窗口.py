# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 03:21:42 2019

@author: 10539
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        record=[]
        lis=[]
        for i,val in enumerate(nums):
            if lis and lis[0]==i-k:
                lis.pop(0)
            while lis and nums[i]>nums[lis[-1]]:
                lis.pop()
            lis.append(i)
            if i>=k-1:record.append(nums[lis[0]])
        return record