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

Most of the code is under BST because intuitively
    functions take place at the data structure level 
    instead of at the node level. 

TBD: Extensive testing!
