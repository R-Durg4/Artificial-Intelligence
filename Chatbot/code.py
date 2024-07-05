#chatbot
qa={
    "Hi":"Hello",
    "How are you":"Im fine how are you doing today",
    "I have a doubt":"May i help with it?",
    "goodbye":"Thankyou for letting me help. Goodbye."
}
def fibanocci(n):
  fib_series = [0, 1]  # Initialize the series with the first two terms
  while len(fib_series) < n:
      fib_series.append(fib_series[n-1] + fib_series[n-2])
  return fib_series

def getresponse(userinput):
  f=0
  for que,ans in qa.items():
    if userinput.lower()==que.lower():
      return ans
    if "fibanocci" in userinput.lower():
      return "Please provide the required limit "
  return "Sorry i dont have an answer for that"
while True:
  userinput=input("You: ")
  response=getresponse(userinput)
  print("Chatbot: ",response)
  if "fibanocci" in userinput.lower():
    ui=int(input("You: "))
    print("Chatbot: ",fibanocci(ui))
  if userinput=="goodbye":
    break
