"""
The abstract class for implementing a stack.

code written by Bryn Abyan Ghiffar
"""
from typing import Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar('T')

class Stack(ABC, Generic[T]):

    def __init__(self) -> None:
        self.length = 0
    
    @abstractmethod
    def push(self, item : T) -> None:
        """pushes an element to the top of the stack"""
        pass

    @abstractmethod
    def pop(self) -> T:
        """pops item from the top of the stack"""
        pass           

    @abstractmethod
    def peek(self) -> T:
        """peeks at the element at the top of the stack"""
        pass

    def __len__(self) -> int:
        """returns the amount of objects in the stack"""
        return self.length
    
    def is_empty(self) -> bool:
        """returns True if the stack is empty returns False otherwise"""
        return len(self) == 0
    
    @abstractmethod
    def is_full(self) -> bool:
        """returns True is full and returns False otherwise"""
        pass
    
    def clear(self) -> None:
        """empties the contents of the stack"""
        self.length = 0


