#!usr/bin/python3

from selenium import webdriver
import time
import urllib
    
x = input("Enter the URL: ")
refreshrate = input("Enter the number of seconds: ")
refreshrate = int(refreshrate)
driver = webdriver.Firefox()
driver.get("https://"+x)

while True:
    time.sleep(refreshrate)
    driver.refresh()
