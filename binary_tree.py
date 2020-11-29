"""
Binary tree class written by Bryn Abyan Ghiffar.
Binary tree class has the append functionality
and the remove functionality.

"""

from typing import TypeVar, Generic
from link_queue import LinkQueue

T = TypeVar('T')

class BinaryTreeNode(Generic[T]):
    
    def __init__(self, key : T, item : T) -> None:
        self.item = item
        self.key = key
        self.right = None
        self.left = None

class BinaryTreeIterator(Generic[T]):

    def __init__(self, root : BinaryTreeNode) -> None:
        self.queue = LinkQueue()
        self.init_aux(root)

    def init_aux(self, current : BinaryTreeNode) -> BinaryTreeNode:
        if current.left is not None:
            self.init_aux(current.left)
        self.queue.append(current.key)
        if current.right is not None:
            self.init_aux(current.right)
    
    def __iter__(self):
        return self
    
    def __next__(self) -> T:
        if self.queue.is_empty():
            raise StopIteration
        return self.queue.serve()

class BinaryTree(Generic[T]):

    def __init__(self) -> None:
        """
        initializes the binary tree class 
        with None root.

        Note : tree only allows a single datatype
        to be stored.
        """
        self.root = None
    
    def setitem_aux(self, current : BinaryTreeNode, key : T, item : T) -> BinaryTreeNode:
        """
        Auxiliary function for self.appends(item)
        """
        if current is None:
            # If we have found an empty spot
            # return the Binary tree node.
           return BinaryTreeNode(key, item)
        else:
            if current.key > key:
                current.left = self.setitem_aux(current.left, key, item)
                current.left = self.do_balance(current.left)
            elif current.key < key:
                current.right = self.setitem_aux(current.right, key , item)
                current.right = self.do_balance(current.right)
            else:
                # In this implementation duplicates are not allowed.
                return BinaryTreeNode(key, item)
            return current

    def __setitem__(self, key : T, item : T) -> None:
        """
        appends an item to the tree.
        """
        self.root = self.setitem_aux(self.root, key, item)
        self.root = self.do_balance(self.root)
    
    def __getitem__(self, key : T) -> T:
        """returns the item based on the specified key"""
        return self.getitem_aux(self.root, key)

    def getitem_aux(self, current : BinaryTreeNode, key : T) -> T:
        """auxiliary function for self.__getitem__()"""

        if current is None:
            raise ValueError("Item not in dictionary")
        else:
            if key < current.key:
                return self.getitem_aux(current.left, key)
            elif key > current.key:
                return self.getitem_aux(current.right, key)
            else: # key found
                return current.item

    def print_tree(self) -> None:
        """
        prints the structure of the tree.
        """
        self.print_tree_aux(self.root, 0)

    def print_tree_aux(self, current : BinaryTreeNode, indentation_level : int) -> None:
        if current is None:
            return
        else:
            print('-' * indentation_level + '-> ' + str(current.key))
            self.print_tree_aux(current.left, indentation_level + 1)
            self.print_tree_aux(current.right, indentation_level + 1)
    
    def __contains__(self, key : T) -> None:
        """
        Returns True if item is contained within the tree,
        false otherwise.
        """
        return self.contains_aux(self.root, key)

    def contains_aux(self, current : BinaryTreeNode, key : T) -> bool:
        """
        Auxiliary function for self.__contains__()
        """
        if current is None:
            return False
        else:
            if current.key == key:
                return True
            elif key < current.key:
                return self.contains_aux(current.left, key)
            elif key > current.key:
                return self.contains_aux(current.right, key)
    
    def __len__(self) -> int:
        """
        Returns the height or depth of the tree.
        """
        return self.len_aux(self.root)

    def len_aux(self, current : BinaryTreeNode) -> int:
        """
        Auxiliary function for self.__len__()
        """
        if current is None:
            return -1
        else:
            return max(self.len_aux(current.left), self.len_aux(current.right)) + 1

    def get_balance(self, current : BinaryTreeNode) -> int:
        """
        Return the balance value of a particular node in the tree.
        """
        if current is None:
            return 0
        else:
            return self.len_aux(current.left) - self.len_aux(current.right)

    def is_balanced(self, current : BinaryTreeNode) -> bool:
        """
        Returns true if a node is within the balance interval.
        """
        return abs(self.get_balance(current)) <= 1

    def is_tree_balanced(self) -> bool:
        """
        Returns true if the tree is balanced.
        """
        return self.is_balanced(self.root)
    
    def delete_aux(self, current : BinaryTreeNode, key : T) -> BinaryTreeNode:
        """auxiliary function for remove"""
        if current is None:
            raise ValueError('item does not exist in the tree.')
        else:
            if key < current.key:
                current.left = self.delete_aux(current.left, key)
                current.left = self.do_balance(current.left)
            elif key > current.key:
                current.right = self.delete_aux(current.right, key)
                current.right = self.do_balance(current.right)
            else: # item is found
                if current.left is None:
                    return current.right
                elif current.right is None:
                    return current.left
                else: # This is where the node has both children
                    # get successor node.
                    successor_node = self.get_successor(current)
                    
                    # take advantage that every item appears once.
                    self.delete_aux(current, successor_node.key)

                    successor_node.right = current.right
                    successor_node.left = current.left

                    return successor_node
            return current

    def remove(self, key : T) -> None:
        """removes the item from the tree"""
        self.root = self.delete_aux(self.root, key)
        self.root = self.do_balance(self.root)

    def get_minimum(self, current : BinaryTreeNode) -> BinaryTreeNode:
        """
        returns the node with the minimum key.
        """
        if current.left is None:
            return current
        else:
            return self.get_minimum(current.left)
    
    def get_successor(self, current : BinaryTreeNode) -> BinaryTreeNode:
        """returns the successor node in the tree of the
        input node."""
        return self.get_minimum(current.right)
    
    def right_rotation(self, current : BinaryTreeNode) -> BinaryTreeNode:
        """applies the right rotation towards
        the input node in the tree."""
        assert current is not None
        assert current.left is not None
        temp = current.left
        current.left = temp.right
        temp.right = current
        return temp
    
    def left_rotation(self, current : BinaryTreeNode) -> BinaryTreeNode:
        """applies the left rotation towards the input
        node in the tree."""
        assert current is not None
        assert current.right is not None
        temp = current.right
        current.right = temp.left
        temp.left = current
        return temp

    def do_balance(self, current : BinaryTreeNode) -> BinaryTreeNode:
        """applies the left or right rotation or does nothing
        depending on whether the node is left heavy or right heavy."""
        bal_val = self.get_balance(current)
        if bal_val > 1: # This means that the node is left heavy
            # if node is left heavy then do right rotation
            return self.right_rotation(current)
        elif bal_val < -1: # This means that the node is right heavy
            return self.left_rotation(current)
        else:
            return current
    
    def __iter__(self) -> BinaryTreeIterator:
        return BinaryTreeIterator(self.root)



if __name__ == '__main__':
    my_tree = BinaryTree()
    for i in range(10 ** 4):
        my_tree[i] = i ** 2
    for key in my_tree:
        print(my_tree[key])
    my_tree.print_tree()