#!/usr/bin/python3

import subprocess
from Live import load_game,welcome
from MemoryGame import is_list_equal

          # MAIN #

if __name__ == "__main__":

 welcome()
 game=load_game()
 print("\n  GAME IS " + game )
 if game == "1" :
   subprocess.call("./MemoryGame.py", shell=True)
