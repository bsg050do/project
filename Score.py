#!/usr/bin/python3
#Score.py 

from Utils import scorefile, screen_cleaner, bad_return_code

def add_score(difficulty):
 try:
   with open(scorefile,"r") as f:
      current_score=int(f.read())
      f.close()
      print(f"Score before winning is" , int(current_score))
      points_of_winning = (difficulty * 3) + 5
      Score = current_score + points_of_winning
      print(f"Score after winning is" , int(Score))
      with open(scorefile,"w") as f:
        f.write(str(Score))
        f.close()
 except bad_return_code:  
    print("Can't open scorefile")


          # MAIN #

if __name__ == "__main__":

  add_score()
