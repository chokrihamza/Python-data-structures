# implemenation of the breadth first search
# let's just do it  yummpy
# our graph using hash table
graph={
    0:[1,2,3],
    1:[0,2],
    2:[0,1,4],
    3:[0],
    4:[2]
}

def bfs(graph,root):
    queue=[]
    visited=[]
    queue.append(root)
    idx=0
    while idx<len(queue):
        current=queue[idx]
        visited.append(current)
        idx+=1
        for node in graph[current]:
            if node not in visited:
                queue.append(node)
    return visited


print(bfs(graph,3))