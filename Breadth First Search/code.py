#bfs
g={}
while True:
  edge=input("enter edges in p-c format and enter done to exit").split()
  if 'done' in edge: #all nodes entered
    break
  p,c = edge
  if p not in g:  #if p not traversed yet
    g[p]=[]
  g[p].append(c)  
print(g)
def bfs(g,start):
  visited=set() #to keep track of visited nodes
  q=[start]
  while(q):
    node=q.pop(0) #pop out first element from queue and check if it is traversed
    if node not in visited:
      print(node)
      visited.add(node)
      q.extend(n for n in g.get(node,[]) if n not in visited)
bfs(g,next(iter(g)))

