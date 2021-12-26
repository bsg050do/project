#!/usr/bin/python3

import random,time,os
from Score import add_score
from Utils import screen_cleaner

def generate_sequence(difficulty):

   randomlist = []
   for num in range(0, difficulty):
     num = random.randint(1,101)
     randomlist.append(num)
   print(randomlist)
   return randomlist

def get_list_from_user():

   print(f"\nPlease provide" , difficulty , "numbers " )
   mylist = []
   count=1
   while count < difficulty+1:
     mynum=int(input())
     mylist.append(mynum)
     print(f"Please next number" )
     count += 1
   print(f"\n Your list is " ,mylist)
   return mylist

def is_list_equal(mylist,randomlist):

  if mylist == randomlist :
     res=True
  else:
     res=False
  return res
    

          # MAIN #

if __name__ == "__main__":

  difficulty=int(input("Please choose list length of random numbers "))
  randomlist = generate_sequence(difficulty)
  time.sleep(0.7)
  #os.system('clear')
  screen_cleaner()
  mylist = get_list_from_user()

  res = is_list_equal(randomlist, mylist)
  if res == True:
     print("\nYOU WON!\n")
     add_score(difficulty)
     
  elif res == False:
     print("\nYou lost")
