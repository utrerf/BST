This is an implementation of a binary search tree (BST).

BST's are composed of nodes that look like this:

           parent
             |   
            key
           |   |
  left child   right child


Key property (invariant) of BST's

    Every single node, call it N, is such that:
        N.left.key  <  N.key  <  N.right.key

BST's are powerful because they allow us to perform
    search in O(h), where h is the height of the BST

=========

What would I do differently:
    Reorganize the functions in different classes:
        Currently we have functions such as insert and delete at the
        BSTNode level. This is a problem because intuitively you want to 
        insert or delete nodes in the BST, NOT in the node itself. Therefore
        it would be much better to actually have bare minimum functions at
        the node and then have data structure functions at the BST class lvl

        As a result of this problem, the coding of insert and delete cannot 
        assume that the call is being made at the root node, making the code
        super messy and hard to read. This root assumption would hold if instead
        the BST class made the call instead of BSTNode


