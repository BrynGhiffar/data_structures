"""
linked stack implementation
using the Stack() class from
abstract_stack.py as an abstract class
(structure for implementation)

code written by Bryn Abyan Ghiffar
"""

from typing import TypeVar, Generic
from abstract_stack import Stack

T = TypeVar('T')

class LinkedStackNode:

    def __init__(self, item : T) -> None:
        self.item = item
        self.next = None

class LinkedStack(Stack):
    
    def __init__(self) -> None:
        Stack.__init__(self)
        self.top = None
    
    def push(self, item : T) -> None:
        """pushes an object to the top of the stack
        complexity:
        - best case: O(1)
        - worst case: O(1)"""
        new_node = LinkedStackNode(item)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def pop(self) -> T:
        """pops an object from the top of the stack
        complexity:
        - best case: O(1)
        - worst case: O(1)"""
        if self.is_empty():
            raise Exception("Stack is empty")
        res = self.top.item
        self.top = self.top.next
        self.length -= 1
        return res

    def peek(self) -> T:
        """peeks an item at the top of the stack.
        complexity:
        - best case: O(1)
        - worst case: O(1)"""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.item

    def is_full(self) -> bool:
        """Always returns False because LinkedList() can never
        be full as there is no fixed memory size allocated to it.
        complexity:
        - best case: O(1)
        - worst case: O(1)
        """
        return False
    
    def clear(self) -> None:
        """clears all the items from the LinkedStack()
        complexity:
        - best case: O(1)
        - worst case: O(1)"""
        Stack.clear(self)
        self.top = None

if __name__ == '__main__':
    my_stack = LinkedStack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(4)
    my_stack.push(5)
    my_stack.push(6)
    my_stack.push(7)
    while not my_stack.is_empty():
        print(my_stack.pop())



