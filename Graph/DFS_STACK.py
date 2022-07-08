# we are going to use a stack as a data structure

graph={
    'A':['B','C','D'],
    'B':['E'],
    'C':['D','E'],
    'D':['A','C'], # or just 'D':[]
    'E':['B','C'] # or just 'E':[]
}

def dfs(graph,root):
    visited=[]
    stack=[]
    stack.append(root)
    while stack:
        current=stack.pop()
        if current not in visited:
           visited.append(current)
           for node in graph[current]:
                if node not in visited:
                  stack.append(node)

    return visited


print(dfs(graph,'A'))