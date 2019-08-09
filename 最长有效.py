# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 01:50:16 2019

@author: 10539
"""

class Solution:

    def longestValidParentheses(self, s):

        st, b = [], [0]*len(s)
        for i, val in enumerate(s):
            if val == '(':
                st.append(i)
            elif st:
                b[st.pop()], b[i] = 1, 1

        c, mc = 0, 0
        for i in b:
            if i:
                c += 1
            else:
                mc = max(c, mc)
                c = 0

        return max(c, mc)

l=Solution()
print(l.longestValidParentheses("()((()()())"))
        