"""Apply the right technique to overcome the inefficiency
We can limit the number of iterations required for common operations
 like find, insert and update by organizing our data in the following structure,
  called a binary tree:"""
#It's called a tree because it vaguely like an inverted tree trunk with branches.

#1-The word "binary" indicates that each "node" in
#1- the tree can have at most 2 children (left or right).
#2-Nodes can have 0, 1 or 2 children. Nodes
#2-that do not have any children are sometimes also called "leaves".
#3-The single node at the top is called the
#3-"root" node, and it typically where operations like search, insertion etc. begin.

#**********************__Balanced Binary Search Trees__*****************************************
#For our use case, we require the binary tree to have some additional properties:

#1-Keys and Values: Each node of the tree stores a key (a username)
# and a value (a User object). Only keys are shown in
# the picture above for brevity. A binary tree where
# nodes have both a key and a value is often referred to
# as a map or treemap (because it maps keys to values).
#2-Binary Search Tree: The left subtree of any node only contains
# nodes with keys that are lexicographically smaller than the node's key,
# and the right subtree of any node only contains nodes with keys
# that lexicographically larger than the node's key. A tree that satisfies
# this property is called a binary search trees, and it's easy to locate
# a specific key by traversing a single path down from the root note.
#3-Balanced Tree: The tree is balanced i.e. it does not
# skew too heavily to one side or the other. The left and
# right subtrees of any node shouldn't differ in height/depth
# by more than 1 level.
"""
                               jadhesh                         1
                             /            \
                         biraj            sonaksh              2 
                                         /         \
                        /    \
                    aakash     hemanth  siddhant  vishal       3
                    
                    ***        ***       ***       ***          k

Height of a Binary Tree:

level 0 : 1
level 1 : 2
level 2 : 2^2
.
.
.
.
.
level k-1: 2^k-1

if we have N nodes in the tree 

then N=1+2^2+2^3+........+2^k-1=sum(i=0,i=k-1,2^k-1)
N + 1 = 2^k
k=log(N+1)<=log(N)+1

Thus, to store N records we require a balanced binary search tree (BST) of height no larger than log(N) + 1. This is a very useful property,
in combination with the fact that nodes are arranged 
in a way that makes it easy to find a specific key by
following a single path down from the root.

As we'll see soon, the 
**************************
***insert, ***
***find ****
***and update *****
***operations*****************

in a balanced BST have time complexity O(log N) since 
they all involve traversing a single path down from the root of the tree.


"""


class TreeNode:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None











