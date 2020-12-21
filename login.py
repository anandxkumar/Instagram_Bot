from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from bs4 import BeautifulSoup as bs4
import time


class Login:
    def __init__(self,driver,username,password):
        self.driver = driver # So the driver value of this class is equal to the driver value passed onto it
        self.username = username
        self.password = password
    
    def signin(self):
        self.driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher') # It will open the login url of instagram
        
        # what we do is go to userid inspect and again inspect and copy selected css code 
        #then WebDriver will wait max till 10 sec to assign the selector to uid 
        #uid = self.driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input')
        uid = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#loginForm > div > div:nth-child(1) > div > label > input')))
        uid.click() # we click on the input textbox
        uid.send_keys(self.username)#will upload a string in the username box
        #for the password section
        # As we have already loaded the 
        pswd = self.driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
        pswd.click()
        pswd.send_keys(self.password)
        
        # For clicking the button
        
        btn = self.driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button > div')
        btn.click()
        #time.sleep(3)