#!/usr/bin/python3

import random,time,os,requests

def get_money_interval():

   t = []
   t = random.randint(1,100)
   print(t)
   return t

def get_guess_from_user(t,d):

   rate=3.12
   print(rate*t)
   myguess = int(input("Please guess how much shekels in dollars above\n "))
   nisinterval = []
   nisinterval=(rate*(t - (5 - d)), rate*(t - (5 + d)))
   print(nisinterval)

   if myguess > int(nisinterval[1]) and myguess < int(nisinterval[0])  :
    print("\nYou won")
   else:
    print("\nYou lost")
    

          # MAIN #


if __name__ == "__main__":

   d = int(input("Please choose game difficulty level "))
   t = get_money_interval()

   get_guess_from_user(t,d)



