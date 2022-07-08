"""
Question: Write a function to find the length of the shortest path
 between two nodes in a weighted directed graph.
"""
# Solution
# if there are no weights so we can just use BFS
# if there are weights so we use Dijkstra or even A(star)
# in this part we will implement Dijekstra's algorithm
# let's start

# Dijekstra steps:
""" 
1-Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
2-Assign to every node a tentative distance value: set it to zero for our initial
 node and to infinity for all other nodes. Set the initial node as current.[16]
3-For the current node, consider all of its unvisited neighbours and calculate their
 tentative distances through the current node. Compare the newly calculated tentative
  distance to the current assigned value and assign the smaller one. For example, 
  if the current node A is marked with a distance of 6, and the edge connecting it
   with a neighbour B has length 2, then the distance to B through A will be 6 + 2 = 8.
    If B was previously marked with a distance greater than 8 then change it to 8.
     Otherwise, the current value will be kept.
4-When we are done considering all of the unvisited neighbours of the current node,
 mark the current node as visited and remove it from the unvisited set.
  A visited node will never be checked again.
5-If the destination node has been marked visited (when planning a route between
 two specific nodes) or if the smallest tentative distance among the nodes in
  the unvisited set is infinity (when planning a complete traversal; occurs when
   there is no connection between the initial node and remaining unvisited nodes),
    then stop. The algorithm has finished.
6-Otherwise, select the unvisited node that is marked with the smallest tentative distance,
 set it as the new "current node", and go back to step 3.
"""

# first let's create our graph

num_nodes = 6
edges = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]
#print(num_nodes, len(edges))

# let's create our class

class Graph:
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
# now let's instantiate our class

graph=Graph(num_nodes,edges,directed=True,weighted=True)

print(graph)


# update distance function

def update_distance(graph,current,distance,parent=None):
    """update distance of the current node neighbors"""
    neighbors=graph.data[current]
    weights=graph.weight[current]
    for i,node in enumerate(neighbors):
        weight=weights[i]
        if distance[current]+weight<distance[node]:
            distance[node]=distance[current]+weight
            if parent:
                parent[node]=current


# pick_next_node
def pick_next_node(distance,visited):
    """ pick the next unvisited node at the smallest distance"""
    min_distance=float('inf')
    min_node=None
    for node in range(len(distance)):
        if not visited[node] and distance[node]<min_distance:
            min_node=node
            min_distance=distance[node]
    return min_node



# define the function shortest path
def shortest_path(graph,source,dest):
    """ Find the length of the shortest path between source and destination"""
    visited=[False]*len(graph.data)
    distance=[float('inf')]*len(graph.data)
    parent=[None]*len(graph.data)
    queue=[]
    idx=0
    queue.append(source)
    distance[source]=0
    visited[source]=True
    while idx<len(queue) and not visited[dest]:
        current=queue[idx]
        update_distance(graph,current,distance,parent)
        next_node=pick_next_node(distance,visited)
        if next_node is not None:
            visited[next_node]=True
            queue.append(next_node)
        idx+=1
    print(list(enumerate(parent)))
    return distance[dest],distance,parent

# test Dijkstra Algorithme

print(shortest_path(graph,0,5))