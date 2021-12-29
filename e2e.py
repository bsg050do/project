#!/usr/bin/python3
#e2e.py 

import webbrowser, requests, time, subprocess

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_scores_service():

  driver = webdriver.Firefox()
  driver.get('http://0.0.0.0:5000/')
  score_element= driver.find_element_by_id('score') 
  score = score_element.text
  #print(score)
  driver.quit()
  return score

def main_function(currscore):

   currscore = int(currscore)
   if currscore > 1 and currscore < 1000:
     print("0")
   else:
     print("1")


          # MAIN #

if __name__ == "__main__":

  currscore = test_scores_service()
  main_function(currscore)
