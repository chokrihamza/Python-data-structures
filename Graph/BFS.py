# Breadth first search in python

# our graph
# we will make it as a hash table
graph={
    0:[1,2,3],
    1:[0,2],
    2:[0,1,4],
    3:[0],
    4:[2]
}

import collections
def bfs(graph,root):
    visited=set()
    queue=collections.deque([root])
    while queue:
        current=queue.popleft()
        visited.add(current)
        for i in graph[current]:
            if i not in visited:
               queue.append(i)
    print(visited)


# test our function

bfs(graph,4)