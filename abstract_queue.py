"""
Queue abstract class.

code written by Bryn Abyan Ghiffar
"""
from typing import TypeVar, Generic
from abc import ABC, abstractmethod

T = TypeVar('T')

class Queue(Generic[T]):

    def __init__(self) -> None:
        self.length = 0
    
    @abstractmethod
    def serve(self) -> T:
        """serve the object at the front of the queue"""
        pass

    @abstractmethod
    def append(self, item : T) -> None:
        """appends an object at the back of queue"""
        pass
    
    @abstractmethod
    def peek(self) -> T:
        """peeks at the object in front of the queue"""
        pass

    def __len__(self) -> int:
        """returns the length of the Queue"""
        return self.length

    def is_empty(self) -> bool:
        """returns True if the Queue is empty and False
        otherwise"""
        return len(self) == 0

    @abstractmethod 
    def is_full(self) -> bool:
        """returns False if the Queue is empty and True
        otherwise"""
        pass

    def clear(self) -> None:
        """empties the Queue"""
        self.length = 0


