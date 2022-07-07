"""
Graph Algorithms (BFS, DFS, Shortest Paths) using Python

*Graph Data Strucutre:
   -Adjacency Lists
   -Adjacency Matrix

"""

# create our class Graph
# Note don't use the method []*10
#this generate a problem
# example

#list=[0]*10
#list[0]=1
#print(list)
# for the example above it works fine
# let's try the next example
list1=[[]]*10
list1[0].append(1)
list1[0].append(2)
#print(list1)
# the change hapend in all the lists 'cause there is just one object
# the outer list point to the same lists
# so don't use this method to create a list of empty list
#---------------------------------------------------------------------
# insted you can use list(range)
# example

#print(list(range(10)))
# or just
#print([ _*2 for _ in range(10)])
# so you can use
l2=[[] for _ in range(10)]
#print(l2)
# now if we try .append this will work fine
# and our code will be pretty fine
# let's test it
l2[0].append(10)
#print(l2)
#so it works fine
#--------------------------------------------------------------------
num_nodes=5
edges=[(0,1),(0,4),(1,4),(1,3),(1,2),(2,3),(3,4)]
num_nodes , len(edges)
"""
for n1,n2 in edges:
    print(n1,n2)
"""

# to make the representation more awesome
# let's take a look to enumerate
# print(enumerate) it self return just an object
#print(enumerate([10,2,3,4,5,7,20,14]))

# now let's itirate through it
""" 
for _ in enumerate([10,[2,3],3,4,5,7,20,14]):
    print(_)

"""


class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data =[[] for _ in range(num_nodes)]
        for n1,n2 in edges :
            # insert it into the right lists
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    # Add an edge from a graph represented as a adjacency list
    def addEdge(self,origin,dest):
        self.data[origin].append(dest)
        self.data[dest].append(origin)

    # remove an edge from a graph represented as a adjacency list.

    def removeEdge(self, origin, destination):
        for i in range(len(self.data[origin])):
            if self.data[origin][i] == destination:
                self.data[origin].pop(i)
                break
        for i in range(len(self.data[destination])):
            if self.data[destination][i] == origin:
                self.data[destination].pop(i)
                break

    # let's make the representation awosome
    def __repr__(self):
        return '\n'.join([ "{}: {}".format(n,neighbors) for n,neighbors in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()
# yesss let's make an instance of the graph

graph1=Graph(num_nodes,edges)

# let's see the data in the graph , the adjacency lists
""" 
for x in enumerate(graph1.data):
    print(x)

[print(x) for x in graph1.data]
"""

#-----------------------------------TODO-----------------------------------------------------
""" 

Question: Write a function to add an edge to a graph represented as an adjacency list.

Question: Write a function to remove an edge from a graph represented as a adjacency list.

"""




#-----------------------------------TODO-----------------------------------------------------

# test the addEdge function

graph1.addEdge(0,3)

#print(graph1)

# test the remove function
graph1.removeEdge(0,3)
#print(graph1)
# Next representation Adjacency Matrix
#--------------------------------Adjacency Matrix----------------------------------------

# Adjacency matrix representation using python

class Graph2:
    # initialize the matrix
    def __init__(self,size):
        self.adjMatrix=[]
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size=size

    # add edges
    def add_edge(self,v1,v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
    # remove edges
    def remove_edge(self,v1,v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        print(self.adjMatrix)

# let's test our class Graph2

g = Graph2(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
#g.print_matrix()


#-----------------------------------Graph Traversal---------------------------------------


#------------------------------Breadth-First-Search --------------------------------------------

def BFS(Graph,root):
    queue=[]
    discovered=[False]*len(Graph.data)
    distance=[None]*len(Graph.data)
    parent=[None]*len(Graph.data)
    discovered[root]=True
    distance[root]=0
    queue.append(root)
    # in python list doesn't support de dequeue
    idx=0
    while idx<len(queue):
        # dequeue
        current=queue[idx]
        idx+=1
        for node in Graph.data[current]:
            if not discovered[node]:
                distance[node]=1+distance[current]
                parent[node]=current
                discovered[node]=True
                queue.append(node)

    return queue,distance,parent



#print(BFS(graph1, 0))

#------------------------------Breadth-First-Search-using hash table in python --------------------------------------------

import collections

Graph_hash={
    0:[1,2,3],
    1:[0,2],
    2:[0,1,4],
    3:[0],
    4:[2]
}

Graph_hash2={
    0:[1,4],
    1:[0,2,3,4],
    2:[1,3],
    3:[1,2,4],
    4:[0,1,3]
}


def bfs_hash(Graph,root):
    visited=set()
    queue=collections.deque([root])
    while queue:
        node=queue.popleft()
        visited.add(node)
        for i in Graph[node]:
            if i not in visited:
                queue.append(i)
    print(visited)

#bfs_hash(Graph_hash,0)

#------------------------------Depth-First-Search-using in python --------------------------------------------

def dfs(Graph, root):
    stack = []
    discovered = [False] * len(Graph.data)
    stack.append(root)
    result = []
    while len(stack) > 0:
        current = stack.pop()
        if not discovered[current]:
            discovered[current] = True
            result.append(current)
            for node in Graph.data[current]:
                if not discovered[node]:
                    stack.append(node)

    return result

#-------------------------------------Weighted Graphs ------------------------------------------------------
# Graph with weights
num_nodes5 = 9
edges5 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6),
          (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]

print(num_nodes5, len(edges5))

#-------------------------------------Directed Graphs -------------------------------------------------
num_nodes6 = 5
edges6 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]
print(num_nodes6, len(edges6))

""" 
Question: Define a class to represent weighted and directed graphs in Python.

"""


class Graph_directed_weighted:
    def __init__(self, num_nodes, edges, directed=False, weighted=False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        for edge in edges:
            if self.weighted:
                # include weighted
                node1, node2, weight = edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            else:
                # work without weighted
                node1, node2 = edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)

    def __repr__(self):
        result = ""
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weight)):
                result += "{}:{} \n".format(i, list(zip(nodes, weights)))
        else:
            for i, nodes in enumerate(self.data):
                result += "{}:{} \n".format(i, nodes)

        return result


# test code
graph3=Graph_directed_weighted(num_nodes5,edges5,weighted=True)

#print(graph3)

graph4=Graph_directed_weighted(num_nodes6,edges6,directed=True)
#print(graph4)


