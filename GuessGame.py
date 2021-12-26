#!/usr/bin/python3

import random

def generate_number():

   difficulty=int(input("Please choose game highest difficulty level "))
   print(f"difficulty is" ,difficulty)
   secretnum=(random.randint(0, difficulty))
   print(secretnum)
   return secretnum

def get_guess_from_user():

   myguess=int(input("Please guess secretnum "))
   print(f"you guessed" ,myguess)
   return myguess

def compare_results(myguess, secretnum):
  if myguess == secretnum:
     res=True
  else:
     res=False
  return res

def play(res):
  if res == True:
     print("\nYou won")
  elif res == False:
     print("\nYou lost")
  return res

    
          # MAIN #


if __name__ == "__main__":

  secretnum = generate_number()
  myguess =  get_guess_from_user()
  res = compare_results(myguess, secretnum)
  play(res)

