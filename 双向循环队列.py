# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 03:20:57 2019

@author: 10539
"""

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.lis=[None]*k
        self.head=0
        self.end=0
        self.k=k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if  self.isFull():
            return False
        else:
            self.lis[(self.head-1)%self.k]=value
            self.head=(self.head-1)%self.k
            return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.lis[(self.end+1)%self.k]=value
            self.end=(self.end+1)%self.k
            return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.lis[self.head]=None
            self.head=(self.head+1)%self.k
            return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.lis[self.end]=None
            self.end=(self.end-1)%self.k
            return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            return self.lis[self.head]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            return self.lis[self.end]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.head==self.end

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if self.end-self.head==self.k-1 or self.end-self.head==-1:
            return 1
        else:
            return 0
