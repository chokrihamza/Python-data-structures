# Depth first search recursivly
# our graph
# blind search methods
graph={
    'A':['B','C','D'],
    'B':['E'],
    'C':['D','E'],
    'D':['A','C'], # or just 'D':[]
    'E':['B','C'] # or just 'E':[]
}
visited=set()
def dfs(visited,graph,root):
   if root not in visited:
       print(root)
       visited.add(root)
       for neighbor in graph[root]:
           dfs(visited,graph,neighbor)

dfs(visited,graph,'A')