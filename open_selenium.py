#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get('http://0.0.0.0:5000/')

score_element= driver.find_element_by_id('score') 
score = score_element.text
print(score)

driver.quit()
