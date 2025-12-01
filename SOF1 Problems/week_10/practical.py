"""
Collection of exercises from week 10.
Author: Ethan Davis
"""

from linkednode import LinkedNode

class LinkedStack:

    def __init__(self):
        self._top = None
        self._size = 0

    def __str__(self):
        if self._top is None:
            return "LinkedStack([])"
        else:
            return "LinkedStack([" + str(self._top) + "])"
        
    def __len__(self):
        return self._size
        
    def push(self, value):
        if self._top is None:
            self._top = LinkedNode(value)
        else:
            new_top = LinkedNode(value)
            new_top._next = self._top
            self._top = new_top
        self._size += 1
    
    def pop(self):
        if self._size == 0:
            raise ValueError("Stack is empty")
        else:
            popped = self._top
            self._top = self._top._next
            popped._next = None
            self._size -= 1
            return popped
        
    def peek(self):
        if self._size == 0:
            raise ValueError("Stack is empty")
        else:
            return self._top.data
        
    def isempty(self):
        if self._size == 0:
            return True
        else:
            return False
        
class LinkedQueue:

    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def __str__(self):
        if self._size == 0:
            return "LinkedQueue([])"
        else:
            return "LinkedQueue([" + str(self._front) + "])"
    
    def enqueue(self, value):
        if self._front is None:
            self._front = LinkedNode(value)
            self._back = self._front
            self._size += 1
        else:
            new_back = LinkedNode(value)
            self._back._next = new_back
            self._back = new_back
            self._size += 1

    def pop(self):
        if self._size == 0:
            raise ValueError("Queue is empty")
        else:
            popped = self._front
            self._front = self._front._next
            popped._next = None
            self._size -= 1
            return popped

def main():
    newQ = LinkedQueue()
    newQ.enqueue("first"), newQ.enqueue("second")
    print(newQ)
    print(newQ.pop(), newQ, newQ._size)

if __name__ == "__main__":
    main()