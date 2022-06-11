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
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


Node0=TreeNode(3)
Node1=TreeNode(4)
Node2=TreeNode(5)
Node0.right=Node1
Node0.left=Node2
#print(Node0.key,Node0.left.key,Node0.right.key)

# generate this tree using tuples
"""
                             2
                            /  \
                           3    5
                          /    /  \
                         1    3    7
                               \   / \
                                4  6  8

"""
tree_tuple=((1,3,None),2,((None,3,4),5,(6,7,8)))

def parse_tuple(data):
    #print(data)
    if isinstance(data,tuple) and len(data)==3:
        node=TreeNode(data[1])
        node.left=parse_tuple(data[0])
        node.right=parse_tuple(data[2])
    elif data is None:
        node=None
    else:
        node=TreeNode(data)

    return node

tree2=parse_tuple(tree_tuple)
#print( isinstance(tree2,TreeNode))

# convert tree to tuple
def tree_to_tuple(node):
   if isinstance(node,TreeNode):
        # base case if tree node has no left and right sub_tree
        if node.left is None and node.right is None:
            return node.key

        return (tree_to_tuple(node.left),node.key,tree_to_tuple(node.right))

#print(tree_to_tuple(tree2))

#create a helper function to display all the
# keys in a tree-like structure for easier visualization.
def display_keys(node,space='\t',level=0):
    # base case
    # if the node is empty
    if node is None:
        print(space*level+'0')
        return
    #if the node is a leaf:
    if node.left is None and node.right is None :
        print(space*level+str(node.key))
        return
    # if the node has a children

    display_keys(node.right, space, level + 1)
    print(space*level+str(node.key))
    display_keys(node.left, space, level + 1)


#display_keys(tree2,'   ')


# traversing a binary tree
# three types of traversing
# 1- inorder
# 2- preorder
# 3- postorder

# define a funtion to traverse the tree inorder



def traverse_in_order(node):
     if node is None:
         return []
     return(
         traverse_in_order(node.left)+[node.key]+traverse_in_order(node.right)
     )


#print(traverse_in_order(tree2))


# define a funtion to traverse the tree preorder


def traverse_pre_order(node):
    if node is None :
        return []
    return(
        [node.key]+traverse_pre_order(node.left)+traverse_pre_order(node.right)
    )

#print(traverse_pre_order(tree2))

# define a funtion to traverse the tree postorder
def traverse_post_order(node):
    if node is None :
        return []
    return(
        traverse_pre_order(node.left)+traverse_pre_order(node.right)+[node.key])

#print(traverse_post_order(tree2))



#print(tree_height(tree2))


def minDepth(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    if node.left is None:
        return minDepth(node.right)+1
    if node.right is None:
        return minDepth(node.left)+1
    return min(minDepth(node.left),minDepth(node.right))+1

print(minDepth(tree2))

def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)

#print(tree_size(tree2))

#Diameter of Binary Tree
# 1 first create a function to calculate the height
#height and size of a binary tree
def tree_height(node):
    if node is None:
        return 0
    return 1+max(tree_height(node.left),tree_height(node.right))

# define a function to calculate the diameter

def diameter(node):
    if node is None:
        return 0
    # claculate the left and right hight
    lheight=tree_height(node.left)
    rheight=tree_height(node.right)
    # calcualte the diameter recursively for each subtree
    ldiameter=diameter(node.left)
    rdiameter=diameter(node.right)
    return max(lheight+rheight,max(ldiameter,rdiameter))

#print(diameter(tree2))

# define a class containing all the function

class TreeNodeGenerator():
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))

    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        if self is None:
            return []
        return (TreeNode.traverse_in_order(self.left) +
                [self.key] +
                TreeNode.traverse_in_order(self.right))

    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space * level + '∅')
            return

            # If the node is a leaf
        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return

        # If the node has children
        display_keys(self.right, space, level + 1)
        print(space * level + str(self.key))
        display_keys(self.left, space, level + 1)

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right)

    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node

#Binary Search Tree (BST)
#A binary search tree or BST is a binary tree that satisfies the following conditions:

# 1-The left subtree of any node only contains nodes with keys less than the node's key
# 2-The right subtree of any node only contains nodes with keys greater than the node's key
#------------------------------------------------------------------------------------------------------
#QUESTION 8: Write a function to check if a binary tree is a binary search tree (BST).

#QUESTION 9: Write a function to find the maximum key in a binary tree.

#QUESTION 10: Write a function to find the minimum key in a binary tree.
#------------------------------------------------------------------------------------------------------

def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True,None,None
    is_bst_l,min_l,max_l=is_bst(node.left)
    is_bst_r,min_r,max_r=is_bst(node.right)

    is_bst_node=(is_bst_l and is_bst_r and (max_l is None or node.key > max_l)
                 and (min_r is None or node.key < min_r))
    min_key=min(remove_none([min_l,node.key,min_r]))
    max_key=max(remove_none([max_l,node.key,max_r]))

    return is_bst_node,min_key,max_key





tree3 = parse_tuple((('aakash', 'biraj', 'hemanth')  , 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))
print(is_bst(tree3))


#Storing Key-Value Pairs using BSTs
class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class User:
    def __init__(self,username,name,email):
        self.username=username
        self.name=name
        self.email=email
        print('User created!')
    def introduce_yourself(self,guest_name):
        print("Hi {}, I'm {}! Contact me at {} .".format(guest_name, self.name, self.email))

    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')


# Level 0
tree = BSTNode(jadhesh.username, jadhesh)


print(tree.key,tree.value)

# Level 1
tree.left = BSTNode(biraj.username, biraj)
tree.right = BSTNode(sonaksh.username, sonaksh)
tree.left.left = BSTNode(aakash.username, aakash)
tree.left.right = BSTNode(hemanth.username, hemanth)
tree.right.left = BSTNode(siddhant.username, siddhant)
tree.right.right = BSTNode(vishal.username, vishal)
print(tree.left.key, tree.left.value, tree.right.key, tree.right.value)

#display_keys(tree,'          ')

#insert in to a BST tree

#QUESTION 11: Write a function to insert a new node into a BST.

def insert(node,key,value):
    if node is None:
        node=BSTNode(key,value)
    elif key<node.key:
        node.left=insert(node.left,key,value)
        node.left.parent=node
    elif node.key<key:
        node.right=insert(node.right,key,value)
        node.right.parent=node
    return node

# use it to create our tree
tree_with_insertion = insert(None, jadhesh.username, jadhesh)

insert(tree_with_insertion, biraj.username, biraj)
insert(tree_with_insertion, sonaksh.username, sonaksh)
insert(tree_with_insertion, aakash.username, aakash)
insert(tree_with_insertion, hemanth.username, hemanth)
insert(tree_with_insertion, siddhant.username, siddhant)
insert(tree_with_insertion, vishal.username, siddhant)
"""
                    vishal
          sonaksh
                    siddhant
jadhesh
                    hemanth
          biraj
                    aakash



"""



display_keys(tree_with_insertion,'          ')

# the order of insertion of nodes  change the structure of the resulting tree
tree_with_insertion2 = insert(None, aakash.username, aakash)
insert(tree_with_insertion2, biraj.username, biraj)
insert(tree_with_insertion2, hemanth.username, hemanth)
insert(tree_with_insertion2, jadhesh.username, jadhesh)
insert(tree_with_insertion2, siddhant.username, siddhant)
insert(tree_with_insertion2, sonaksh.username, sonaksh)
insert(tree_with_insertion2, vishal.username, vishal)

display_keys(tree_with_insertion2,'          ')

# Note for this part
""" 
                         vishal
                          ∅
					sonaksh
						∅
				siddhant
					∅
			jadhesh
				∅
		hemanth
			∅
	biraj
		∅
aakash
	∅

(worst case)

Skewed/unbalanced BSTs are problematic because the height of such trees
often ceases to logarithmic compared to the number of nodes in the tree.
For instance the above tree has 7 nodes and height 7.

The length of the path traversed by insert is equal to the height of the 
tree (in the worst case). It follows that if the tree is balanced,
the time complexity of insertion is O(log N) otherwise it is O(N).
 
"""
# We need some technic to balance a tree

hamza = User('hamza', 'hamza chokri', 'hamza@example.com')
alex = User('alex', 'alex doe', 'alex@example.com')
jhon = User('jhon', 'jhon doe', 'jhon@example.com')
jeanique = User('jeanique', 'Jeanique wiel', 'jeanique@example.com')
stieve = User('stieve', 'Stieve jobs', 'stieve@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')



tree_with_insertion3 = insert(None, hamza.username, hamza)
insert(tree_with_insertion3, alex.username, alex)
insert(tree_with_insertion3, jhon.username, jhon)
insert(tree_with_insertion3, jeanique.username, jeanique)
insert(tree_with_insertion3, stieve.username, stieve)
insert(tree_with_insertion3, sonaksh.username, sonaksh)
insert(tree_with_insertion3, vishal.username, vishal)

display_keys(tree_with_insertion3,'          ')


#Updating a value in a BST

#QUESTION 12: Write a function to update the value associated with a given key within a BST

# define a function to find element in a tree

def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)






def update(node,key,value):
    target=find(node,key)
    if target is not None:
        target.value=value


# list all the nodes
# QUESTION 13: Write a function to retrieve all the key-values pairs stored in a BST in the sorted order of keys
def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

print(list_all(tree_with_insertion3))

# Balance a binary tree
# QUESTION 14: Write a function to determine if a binary tree is balanced.
"""
Here's a recursive strategy:

1-Ensure that the left subtree is balanced.
2-Ensure that the right subtree is balanced.
3-Ensure that the difference between heights of left subtree and right subtree is not more than 1.


"""

def is_balanced(node):
    # base case
    if node is None:
        return True,0
    balanced_l,height_l=is_balanced(node.left)
    balanced_r,height_r=is_balanced(node.right)

    balanced=balanced_l and balanced_r and abs(height_l-height_r)<=1
    height=1+max(height_l,height_r)
    return balanced,height

print(is_balanced(tree_with_insertion))

# Check Completeness of a Binary Tree

# breadth first traversal

def isCompleteTree(root):
  queue = [root]
  gap = False
  while queue:
    node = queue.pop(0)
    if not node:
        gap = True
    else:
        if gap:
            return False

        queue.append(node.left)
        queue.append(node.right)
  return True


print(isCompleteTree(tree_with_insertion)) # return True because there is no gap in the tree
print(isCompleteTree(tree_with_insertion3))  # return False because we have  gaps in the tree

#Balanced Binary Search Trees

# QUESTION 15: Write a function to create a balanced BST from a sorted list/array of key-value pairs.

#We can use a recursive strategy here, turning the middle element of the list into the root,
# and recursively creating left and right subtrees.

def make_balanced_bst(data,low=0,heigh=None,parent=None):
    if heigh is None:
        heigh=len(data)-1
    if low>heigh:
        return None

    mid=(low+heigh)//2
    key,value=data[mid]
    root=BSTNode(key, value)
    root.parent=parent
    root.left = make_balanced_bst(data, low, mid - 1, root)
    root.right = make_balanced_bst(data, mid + 1, heigh, root)
    return root

users=[User(username='aakash', name='Aakash Rai', email='aakash@example.com'),
 User(username='biraj', name='Biraj Das', email='biraj@example.com'),
 User(username='hemanth', name='Hemanth Jain', email='hemanth@example.com'),
 User(username='jadhesh', name='Jadhesh Verma', email='jadhesh@example.com'),
 User(username='siddhant', name='Siddhant U', email='siddhantu@example.com'),
 User(username='sonaksh', name='Sonaksh Kumar', email='sonaksh@example.com'),
 User(username='vishal', name='Vishal Goel', email='vishal@example.com')]


data = [(user.username, user) for user in users]

print(data)
print(make_balanced_bst(data))

display_keys(make_balanced_bst(data),'        ')

# Balancing an Unbalanced BST

#  QUESTION 16: Write a function to balance an unbalanced binary search tree.

# We first perform an inorder traversal, then create a balanced BST using the function defined earlier.

def balance_bst(node):
    return make_balanced_bst(list_all(node))

"""
After every insertion, we can balance the tree. This way the tree will remain balanced.

Complexity of the various operations in a balanced BST:

Insert - O(log N) + O(N) = O(N)
Find - O(log N)
Update - O(log N)
List all - O(N)


"""

# A Python-Friendly Treemap
"""
We are now ready to return to our original problem statement.

QUESTION 1: As a senior backend engineer at Jovian, you are tasked with developing a
fast in-memory data structure to manage profile information (username, name and email)
for 100 million users. It should allow the following operations to be performed efficiently:

Insert the profile information for a new user.
Find the profile information of a user, given their username
Update the profile information of a user, given their usrname
List all the users of the platform, sorted by username
You can assume that usernames are unique.

We can create a generic class TreeMap which supports all the operations 
specified in the original problem statement in a python-friendly manner.

"""

#Response
# we define our class TreeMap
class TreeMap():
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, key, value)
            self.root = balance_bst(self.root)
        else:
            update(self.root, key, value)

    def __getitem__(self, key):
        node = find(self.root, key)
        return node.value if node else None

    def __iter__(self):
        return (x for x in list_all(self.root))

    def __len__(self):
        return tree_size(self.root)

    def display(self):
        return display_keys(self.root)

# Self-Balancing Binary Trees and AVL Trees

""" 
A self-balancing binary tree remains balanced after every insertion or deletion. 
Several decades of research has gone into creating self-balancing binary trees, 
and many approaches have been devised :
e.g. 
*B-trees, 
*Red Black Trees
*AVL (Adelson-Velsky Landis) trees.

We'll take a brief look at AVL trees. 
Self-balancing in AVL trees is achieved by tracking the balance factor 
(difference between the height of the left subtree and the right subtree)
for each node and rotating unbalanced subtrees along the path of
insertion/deletion to balance them.

In a balanced BST, the balance factor of each node is either 0, -1, or 1. 
When we perform an insertion, then the balance factor of certain nodes along
the path of insertion may change to 2 or -2.
Those nodes can be "rotated" one-by-one to bring the balance factor back to 1, 0 or -1.

There are 4 different scenarios for balancing, two of which require a single rotation, 
while the others require 2 rotations:
"""


#Summary
""" 
Binary trees form the basis of many modern programming language features (e.g. maps in C++ and Java) and data storage systems (filesystem indexes, relational databases like MySQL). You might wonder if dictionaries in Python are also binary search trees. They're not. They're hash tables, which is a different but equally interesting and important data structure. We'll explore hash tables in a future tutorial.

We've covered a lot of ground this in this tutorial, including several common interview questions. Here are a few more problems you can try out:

1-Implement rotations and self-balancing insertion
2-Implement deletion of a node from a binary search tree
3-Implement deletion of a node from a BST (with balancing)
4-Find the lowest common ancestor of two nodes in a tree (Hint: Use the parent property)
5-Find the next node in lexicographic order for a given node
6-Given a number k, find the k-th node in a BST.




"""






