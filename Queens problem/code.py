#8 queens
n=int(input("Enter number of queens"));
board=[]
for i in range(n):
    board.append([0]*n)

def attack(i,j):
  for k in range(0,n):
    if board[i][k]==1 or board[k][j]==1:
      return True
  for k in range(0,n):
    for l in range(0,n):
      if (k+l==i+j) or (k-l==i-j):
        if board[k][l]==1:
          return True
  return False

def queen(q):
  if q==0:
    return True
  for i in range(0,n):
    for j in range(0,n):
      if(board[i][j]!=1) and (not(attack(i,j))):
        board[i][j]=1
        if(queen(q-1)==True):
          return True
        board[i][j]=0
  return False
queen(n)
for i in board:
  print(i)
