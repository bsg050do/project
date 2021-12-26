#!/usr/bin/python3 
#from MemoryGame import is_list_equal
import MemoryGame 

def welcome():
     name=str(input("What your name ? "))
     print("\nHello " + name + " and welcome to the World of Games \n")
     print("Here you can find many cool games to play \n")

     return

def load_game():
     print("  Please choose a game to play:\n")
     print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
     print("2. Guess Game - guess a number and see if you chose like the computer")
     print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")

     while True:
       game=str(input())
       if game in ("1", "2", "3"):
         print("\nYou selected game " + game)
         break
       else:
         print("Wrong selection")



     print("  Please choose  game difficulty 1 to 5:\n")
     while True:
       difficulty=str(input())
       if difficulty in ("1", "2", "3", "4", "5"): 
         print("\nYou selected difficulty level " + difficulty)
         break
       else:
         print("Wrong selection")


     return game


    
          # MAIN #

if __name__ == "__main__":

  welcome()
  game=load_game()
