# in this part we create our linked list using python class
#We'll implement linked lists which support the following operations:

#Create a list with given elements
#Display the elements in a list
#Find the number of elements in a list
#Retrieve the element at a given position
#Add or remove element(s)


# our first python class
#class Node1:
#   pass
# create object with nothing in it
"""
node1=Node1()
node2=Node1()
node3=node1
print(node1)
print(node2)
print(node3)

class Node():
    def __init__(self):
        self.data=0

Not_Empty_Node1=Node()
Not_Empty_Node1.data=2
Not_Empty_Node2=Node()
Not_Empty_Node2.data=3
Not_Empty_Node3=Node()
Not_Empty_Node3.data=5 """
#print((Not_Empty_Node1.data,Not_Empty_Node2.data,Not_Empty_Node3.data))

class Node():
    def __init__(self, a_number):
        self.data = a_number
        self.next = None

node1 = Node(2)
node2 = Node(3)
node3 = Node(5)
print(node1.data,node2.data,node3.data)


class LinkedList():
    def __init__(self):
        self.head=None
    # add method appending a node
    def append(self,value):
        if self.head is None:
            self.head=Node(value)
        else:
            current_node=self.head
            while current_node.next is not None:
                current_node=current_node.next
            current_node.next=Node(value)
    # Next, let's add a method to print the value in a list.
    def show_elements(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next

    #Let's add the  length
    def length(self):
        result=0
        current=self.head
        while current is not None:
            result+=1
            current=current.next
        return result

    # get_element to get an element at a specific position.
    def get_element(self,position):
        i=0
        current=self.head
        while current is not None:
            if i==position:
                return current.data
            current=current.next
            i+=1
        return None


list1=LinkedList()

#list1.head=Node(5)
#list1.head.next=Node(6)
#list1.head.next.next=Node(7)

#print(list1.head.data, list1.head.next.data, list1.head.next.next.data)

list1.append(100)
list1.append(1000)
list1.append(10000)
list1.show_elements()
print(list1.length())
print(list1.get_element(1))

# create a method inside our class to
# write the output in the screen
# Next, let's add a method to print the value in a list.

#  Reversing a linkedList
list20=LinkedList()
for i in range(1,21):
    list20.append(i)




# program to reverse linkedList
def reverse(LinkedList):
    if LinkedList.head is None:
        return
    current_Node=LinkedList.head
    prev_Node=None
    while current_Node is not None:
        # Track the next node
        next_node = current_Node.next
        #Modify the current node
        current_Node.next=prev_Node
        # Update prev and current
        prev_Node=current_Node
        current_Node=next_node

    LinkedList.head=prev_Node

list20.show_elements()
reverse(list20)
list20.show_elements()