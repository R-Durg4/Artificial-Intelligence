#dfs
g={}
while True:
  edge=input("enter edges in p-c format and enter done to exit: ").split()
  if 'done' in edge:
    break
  p,c = edge
  if p not in g:
    g[p]=[]
  g[p].append(c)
print(g)
def dfs(g,node):
  visited=set()
  stack=[node]
  while stack:
    node=stack.pop()
    if node not in visited:
      print(node)
      visited.add(node)
      stack.extend(reversed(g.get(node,[])))
dfs(g,next(iter(g)))
