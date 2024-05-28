#water jug problem
//Function to find gcd of jug capacities.
def gcd(a,b):
  while b:
    a,b = b,a%b
  return a
//Function to print current jug levels
def display(j1,j2):
  print(f"jug1: {j1} | jug2: {j2}")
//Function to pour water from jug 1 to jug 2
def pour(j1,j2,c1,c2):
  amt=min(j1,c2-j2)
  j1=j1-amt
  j2=j2+amt
  return j1,j2
//Function to start solving the problem
def solve(c1,c2,target):
  j1=j2=0
  while j1!=target and j2!=target:
    if j1==0:
      j1=c1
    elif j2==c2:
      j2=0
    else:
      j1,j2=pour(j1,j2,c1,c2)
    display(j1,j2)
//User input jug capacities and target value t
a=int(input("enter capacity of jug 1 "))
b=int(input("enter capacity of jug2 "))
t=int(input("enter target "))
//Check if problem is solvable or not
if t<=max(a,b) and t%gcd(a,b)==0: //Call solve() if condition is satisfied
  solve(a,b,t)
else:
  print("Target not achievable.")
