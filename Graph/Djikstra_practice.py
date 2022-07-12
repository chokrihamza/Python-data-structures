# first let's take a look to our  graph

num_nodes = 6
edges = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]
#print(num_nodes, len(edges))

# let's create our graph class

class Graph:
    def __init__(self,num_nodes,edges,directed=False,weighted=False):
        self.num_nodes=num_nodes
        self.directed=directed
        self.weighted=weighted
        self.data=[[] for _ in range(num_nodes)]
        self.weight=[[] for _ in range(num_nodes)]
        # reorganize our data inside the instance
        for edge in edges:
            if self.weighted:
                # distruct the content
                node1,node2,weight=edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            else:
                # work without weights
                node1,node2=edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)


    def __repr__(self):
        result=""
        if self.weight:
            for i,(nodes,weights) in enumerate(zip(self.data,self.weight)):
                result+="{}:{} \n".format(i,list(zip(nodes,weights)))
        else:
            for i, nodes in enumerate(self.data):
                result += "{}:{} \n".format(i, nodes)

        return result




#let's see our graph

graph=Graph(num_nodes,edges,directed=True,weighted=True)

#print(graph)


# define update distance function

def update_distance(graph,current,distance,parent=None):
    """" update distance of the current node neighbors """
    neighbors=graph.data[current]
    weights=graph.weight[current]
    for i,node in enumerate(neighbors):
        weight=weights[i]
        if distance[current]+weight<distance[node]:
            distance[node]=distance[current]+weight

            if parent:

                parent[node]=current









# define function select the next node
def pick_next_node(distance,visited):
    """ pick the next unvisited node at the smallest distance """
    min_distane=float('inf')
    min_node=None
    for node in range(len(distance)):
        if not visited[node] and distance[node]<min_distane:
            min_node=node
            min_distane=distance[node]
    return min_node


def shortest_path(graph,source,dest):
    """ find the length of the shortest path between the source and the destination """
    visited=[False]*len(graph.data)
    distance=[float("inf")]*len(graph.data)
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


# test dijekstra algorithme

print(shortest_path(graph,0,5))










