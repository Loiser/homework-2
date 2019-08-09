# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 02:48:05 2019

@author: 10539
"""

class SqQueue(object):
    def __init__(self, maxsize):
        self.queue = [None] * maxsize
        self.maxsize = maxsize
        self.front = 0
        self.rear = 0

    def QueueLength(self):
        return (self.rear - self.front + self.maxsize) % self.maxsize

    def EnQueue(self, data):
        if (self.rear + 1) % self.maxsize == self.front:
            print("The queue is full!")
        else:
            self.queue[self.rear] = data
            self.rear = (self.rear + 1) % self.maxsize

    def DeQueue(self):
        if self.rear == self.front:
            print("The queue is empty!")
        else:
            data = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.maxsize
            return data
    def ShowQueue(self):
        for i in range(self.maxsize):
            print(self.queue[i],end=',')
        print(' ')
if __name__ == '__main__':
   st=SqQueue(3)
   st.EnQueue(4)
   st.EnQueue(3)
   st.ShowQueue()
   st.DeQueue()
   st.DeQueue()
   st.DeQueue()