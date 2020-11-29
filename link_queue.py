"""
LinkQueue class written by Bryn Abyan Ghifar
"""
from typing import TypeVar, Generic
from abstract_queue import Queue

T = TypeVar('T')

class LinkQueueNode(Generic[T]):

    def __init__(self, item : T) -> None:
        self.item = item
        self.next = None

class LinkQueue(Queue, Generic[T]):

    def __init__(self) -> None:
        Queue.__init__(self)
        self.front = None
        self.back = None
    
    def serve(self) -> T:
        """
        serves the object in front of the Queue.
        (pops it off the LinkQueue as well)
        """
        if self.is_empty():
            raise Exception("Queue is empty.")
        res = self.front.item
        self.front = self.front.next
        self.length -= 1

        # Without this piece of code the LinkQueue will
        # still function, but it is better to keep
        # the invariant that if the Queue is empty
        # self.front and self.back is None
        # -----
        if self.is_empty():
            self.back = None 
        # -----
        return res

    def append(self, item : T) -> None:
        """
        appends the object at the end of the LinkQueue()
        """
        new_node = LinkQueueNode(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.back.next = new_node
        self.back = new_node
        self.length += 1
    
    def peek(self) -> T:
        """
        peeks at the object at the front of the
        LinkQueue()
        """
        return self.front.item
    
    def clear(self) -> None:
        """
        Clears the items from the Queue.
        """
        Queue.clear(self)
        self.front = None
        self.back = None

    def is_full(self) -> bool:
        """
        Always returns False since no fixed size
        is allocated to a LinkStack and depends
        on the size of the memory
        """
        return False

if __name__ == '__main__':
    my_queue = LinkQueue()
    my_queue.append(1)
    my_queue.append(2)
    my_queue.append(3)
    my_queue.append(4)
    my_queue.append(5)
    while not my_queue.is_empty():
        print(my_queue.serve())
