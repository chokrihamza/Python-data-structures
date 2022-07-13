# First let's create our graph
num_nodes = 6
edges = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]

# create our class graph containinng the
# description of our graph

class Graph:
    def __init__(self,num_nodes,edges,directed=False,weighted=False):
        self.num_nodes=num_nodes
        # we treat edges at the end
        self.directed=directed
        self.weighted=weighted
        # let's treat our data
        self.data=[[] for _ in range(num_nodes)]
        self.weight=[[] for _ in range(num_nodes)]
        for edge in edges:
            if self.weighted:
                # unpack the data inside the edge
                 node1,node2,weight=edge
                 self.data[node1].append(node2)
                 self.weight[node1].append(weight)
                 if not directed:
                     self.data[node2].append(node1)
                     self.weight[node2].append(weight)
            else:
                # unpack the data inside the edge
                node1, node2 = edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)

    def __repr__(self):
        result=""
        if self.weighted:
            for i ,(nodes,weights) in enumerate(zip(self.data,self.weight)):
                result+="{}:{}\n".format(i,list(zip(nodes,weights)))

        else:
            for i,nodes in  enumerate(self.data):
                result += "{}:{}\n".format(i, nodes)

        return result





# let's test our code

graph=Graph(num_nodes,edges,directed=True,weighted=True)

#print(graph)

# now let's implement Dijekstra algorithm's

# function to update distance
def update_ditance(graph,current,distance,parent=None):
    """ update the distance of the current node neighbors"""
    neighbors=graph.data[current]
    weights=graph.weight[current]
    for i,node in enumerate(neighbors):
        weight=weights[i]
        if distance[current]+weight<distance[node]:
            distance[node]= distance[current]+weight
            if parent:
                parent[node]=current

# function to pick the next node

def pick_next_node(distance,visited):
    """ pick the next unvisited node at the smallest distance"""
    min_distance=float('inf')
    min_node=None
    for node in range(len(distance)):
        if not visited[node] and distance[node]<min_distance:
            min_node=node
            min_distance=distance[node]

    return min_node



def shortest_path(graph,source,dest):
    """ find the shortest path between  the source and the distination """
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
        update_ditance(graph,current,distance,parent)
        next_node=pick_next_node(distance,visited)
        if next_node is not visited:
            visited[next_node]=True
            queue.append(next_node)
        idx+=1
    print(list(enumerate(parent)))
    return distance[dest],distance,parent

# test Dijkstra Algorithme

print(shortest_path(graph,0,5))