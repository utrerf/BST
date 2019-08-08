"""
Description
    This file contains a BST implementation with two classes,
    BSTNode and BST.

Usage
    
    Initialization:
    bst = BST.BST()                 Initialize BST with root=None
    node = BST.BSTNode(None, 5)     BST Node with no parent and key=5
    
    All operations, including insert, delete, find, next_larger, and
    find_min are called at the BST level. For example:

    bst.insert(node)        Inserts node into bst

    Do NOT do this: node.insert()
"""


class BSTNode():
    def __init__(self, parent, key):
        """ Initializes a BST node

        Params:
            parent of node
            key of node
        """
        self.parent = parent
        self.key = key
        self.right = None
        self.left = None

    def __delete(self):
        """ Delete and return self from BST 
        
        This function should NOT be called by users
        and it's only used by BST as a helper function

        It assumes that self has a parent node
        """
        # At least one child is None
        if self.left is None or self.right is None:
            # Reconnect self's parent to self's child (if any)
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            elif self is self.parent.right:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
        else:  
            nxt_larger = self.next_larger()
            self.key, nxt_larger.key = nxt_larger.key, self.key
            return nxt_larger.__delete()

class BST():
    def __init__(self):
        """ Initializes BST """
        self.root = None

    def find(self, k):
        """ Finds and returns node with key k in BST
            Returns None if node is not found

        Params:
            k: key
        """
        current = self.root
        while current is not None and current.key != k:
            if current.key < k: # go left
                current = current.left
            else:               # go right
                current = current.right
        return current

    def find_min(self):
        """ Finds and returns smallest key in BST """
        current = self.root
        if current is not None: # one-time check
            # go left until we find smallest
            while current.left is not None:
                current = current.left
        return current

    def insert(self, k):
        """ Inserts and returns a node with key k

            Returns none if node is not found

            Implementation details:
                1. One-time check if root does not exist
                2. Otherwise compare k vs current.key:
                    2.1 If k > current.key go right
                    2.2 If k < current.key go left
                    2.3 If k == current.key make node=None

                    Both 2.1 and 2.2 check if we should insert
                    or keep going left or right
        """
        node = BSTNode(None, k) 
        if self.root is None:
            self.root = node
       else: 
            current = self.root
            while current is not None:
                if k > current.key:      # Go right
                    if current.right is None:
                        current.right = node
                        node.parent = current
                        current = None
                    else:
                        current = current.right
                elif k < current.key:    # Go left
                    if current.left is None:
                        current.left = node
                        node.parent = current
                        current = None
                    else:              
                        current = current.left
                else:           # key already exists
                    node = None
                    current = None
        return node
        
    def delete(self, k):
        """ Deletes and returns a node with key k 
            if k exists. Otherwise returns None 
            
            Params
                k: key
        """
        node = self.find(k)
        if node is None:        # Nothing to delete
            return None
        elif node is self.root: # Delete root
            temp = BSTNode(None, 0)
            temp.left = node
            deleted = node.__delete()
            self.root = temp.left
            if self.root is not None:
                self.root.parent = None
            return deleted
        else:                   # Delete other node
            return node.__delete()



    def next_larger(self, k):
        """ Returns the node larger than k
        
        Returns None if there are no nodes with key==k
        """
        node = self.find(k)
        if node is not None:
            node = node.right
            while node.left is not None:
                node = node.left
        return node
                

