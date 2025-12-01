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
            self._top = popped._next
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
        
def main():
    pass

if __name__ == "__main__":
    main()