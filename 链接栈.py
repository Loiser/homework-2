# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 01:13:41 2019

@author: 10539
"""

class Node(object):
    def __init__(self,val):
        self.val=val
        self.next=None
        
class Stack(object):
    def __init__(self):
        self.rear = Node(None)
        self.head = self.rear
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def push(self, data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if not self.is_empty():
            current_node = self.head.next
            if self.get_size() == 1:
                self.head.next = None
            else:
                self.head.next = self.head.next.next
            self.size -= 1
            return current_node.val
        else:
            raise IndexError("pop from empty stack")

    def top(self):
        if not self.is_empty():
            return self.head.next.val
        else:
            raise IndexError("stack is empty")
if __name__ == '__main__':
   st=Stack()
   st.push(4)
   st.push(3)
   st.pop()
   st.pop()

    