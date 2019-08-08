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

    def find(self, k):
        """ Finds and returns key in tree rooted at self

        Params:
            k: key
        """
        if self is None:
            return None
        if self.key < k:
            return self.left.find(k)
        elif self.key > k:
            return self.right.find(k)
        else:
            return self

    def find_min(self):
        """ Finds and returns min in tree rooted at self """
        if self.left is None:
            return self
        return self.left.find_min()

    def next_larger(self):
        """ Finds and returns the next larger node in
        the tree rooted at self
        """
        if self.right is None and self.parent.left is not self:
            return None
        next_child = self.right
        while next_child.left is not None:
            next_child = next_child.left
        if next_child is None:
            return self.parent

    def insert(self, node):
        """ Inserts a new node into the subtree rooted at
        this node, assuming that the new node has no parent or children
        """
        if node is None:
            return
        # Zoom out because node is larger or smaller than parent 
        if self.parent is not None:
            if self is self.parent.left and node.key > self.parent.key:
                self.parent.insert(node)
            elif self is self.parent.right and node.key < self.parent.key:
                self.parent.insert(node)
        # Zoom in because node respects boundaries set by parent
        elif self.key > node.key:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)
                
    def delete(self):
        """ Delete and return self from BST """
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            elif self is self.parent.right:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            # When we have a child and no parent cleanup
            else: 
                if self.left is not None:
                    self.left.parent = None
                elif self.right is not None:
                    self.right.parent = None
            return self
        else:
            nxt_larger = self.next_larger()
            self.key, nxt_larger.key = nxt_larger.key, self.key
            return nxt_larger.delete()

class BST():
    def __init__(self):
        self.root = None

    def find(self, k):
        return self.root and self.root.find(k)

    def find_min(self):
        return self.root and self.root.find_min()

    def insert(self, k):
        node = BSTNode(None, k)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)

    def delete(self, k):
        """ Deletes and returns a node with key k 
            if k exists """

        node = self.find(k)
        if node is None:
            return None
        if node is self.root:
            temp = BSTNode(None, 0)
            temp.left = node
            deleted = node.delete()
            self.root = temp.left
            if self.root is not None:
                self.root = None
            return deleted
        else:
            return node.delete()

    def next_larger(self, k):
        """ Returns the node larger than k assuming that k exists """
        node = self.find(k)
        return node and node.next_larger()
