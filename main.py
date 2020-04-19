from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from bs4 import BeautifulSoup as bs4
import time
import login #the other py file we created
import getpages


driver = 0
username = '9315992643'
password = '8860440585'

def main() :
    global driver
    print("running script")
    driver = webdriver.Chrome('F://My Projects/Instagram Bot/chromedriver.exe') # You have to download chromedriver.exe
    l = login.Login(driver,username,password)
    l.signin()
    time.sleep(10)
    # Loads this webpage
    driver.get('https://www.instagram.com/python.learning/')
    #driver.get('https://www.instagram.com/__epic69/')
    
    
    gp = getpages.Getpages(driver)
    #gp.get_followers()
    print("Number of Followers "+ str(gp.get_num_flw()))
    gp.is_public()
    time.sleep(4)
    gp.follow_page()
    time.sleep(10)
    gp.like_post()
    
if __name__ == '__main__':  # If name of the file  is  main() then
    main() 
    
    
