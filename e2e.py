#!/usr/bin/python3
#e2e.py 

import webbrowser, requests, time, subprocess

def main_function():

  RESULT = test_scores_service()
  if RESULT == True:
     print("0")
  elif RESULT == False:
     print("1")
  return RESULT

def test_scores_service():
 try:
   webbrowser.open('http://zil56do01v:5000')
   time.sleep(2)
   response = requests.get('http://zil56do01v:5000')
   res = str(response.content)
   COMMAND = ""
   COMMAND += "echo " + res + " |  awk  '{print $11}' | awk -F\> '{print $2}' | awk -F\< '{print $1}' "
   currscore = int(subprocess.check_output(COMMAND, shell=True).rstrip())
   #print(currscore)
   if currscore > 1 and currscore < 1000:
      ecode=True
   else:
      ecode=False

   return ecode
   
 except :  
    print("Can't open URL")


          # MAIN #

if __name__ == "__main__":

  main_function()
