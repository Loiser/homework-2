# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:07:58 2019

@author: 10539
"""

class Stack():
    def __init__(self,size):
        self.size=size
        self.stack=[]
        self.top=-1

    def push(self,x):
        if self.isfull():
           raise Exception("stack is full")
        else:
            self.stack.append(x)
            self.top=self.top+1

    def pop(self):
        if self.isempty():
            raise Exception("stack is empty")
        else:
            self.top=self.top-1
            self.stack.pop()

    def isfull(self):
        return self.top+1 == self.size
    def isempty(self):
        return self.top == '-1'
    def showStack(self):
        print(self.stack)

if __name__ == '__main__':
   st=Stack(3)
   st.push(4)
   st.push(3)
   st.showStack()
   st.pop()
   st.pop()
   st.pop()
    