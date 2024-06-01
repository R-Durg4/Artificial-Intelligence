#minimax algorithm
def minimax(depth,node,maxplayer,values,alpha,beta):
  if depth==3:
    return values[node]   #currently at last depth so return utility value
  if maxplayer:
    v=float('-inf')
    for i in range(2):
      v=max(v,minimax(depth+1,node*2+i,False,values,alpha,beta))
      alpha=max(v,alpha)
      if alpha>=beta:
        break
    return v
  else:
    v=float('inf')
    for i in range(2):
      v=min(v,minimax(depth+1,node*2+i,True,values,alpha,beta))
      beta=min(beta,v)
      if alpha>= beta:
        break
    return v
values=[2,3,5,9,0,1,7,5]
print("Optimal Value: ",minimax(0,0,True,values,float('-inf'),float('inf')))
