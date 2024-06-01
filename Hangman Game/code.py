#hangman game
import random //to select the game word at random
def guess(word):
  max=7 //max number of attempts
  a=0   
  guessedword= "_"*len(word)     #word to be guessed 

  while a<max and "_" in guessedword:
    print("word to guess is: ",guessedword)
    guess= input("enter a letter").lower()

    if len(guess)!=1 or not guess.isalpha():  #checks if user has entered input in right format
      print("please enter a single alphabet")
      continue
    if guess in word:
      for i in range(len(word)):
        if word[i]==guess:
          guessedword=guessedword[:i]+guess+guessedword[i+1:] #updates the guessed word
      print("correct guess")
    else:
      print("incorrect guess")
      a=a+1
      print("attempts left: ",max-a) #updates number of attempts left
  if "_" not in guessedword:
    print("you win") #whole word is guessed
  else:
    print("you lose. word was: ",word)
words = ["apple","banana","ocean"]
selected= random.choice(words)
guess(selected)
