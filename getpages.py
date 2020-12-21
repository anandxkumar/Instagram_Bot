# To get follower
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from bs4 import BeautifulSoup as bs4
import time

class Getpages :
    def __init__(self,driver):
        self.driver = driver
    
    def get_num_flw(self):  # to get the number of followers of the account
        time.sleep(1)
        flw = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#react-root > section > main')))
        sflw = bs4(flw.get_attribute('innerHTML'),'html.parser')# it is a beautiful soup parser that gets the whole HTML part of the wevpage in a text form , and 2nd arguement will be the parser
        #print(sflw) # print the html text and search for number of followers like 504k and find the class and span(type of statement)
        followers = sflw.findAll('span',{'class':'g47SY'}) #type , class and class name
        f = followers[1].getText()
        #print(f)  # it gives number of followers
        # followers - 0 index- posts , 1 index - followers, 2 index - following
        if 'k' in f :
            f = float(f[:-1])*10**3 # last k is removed like 245k = 245
            return f
        elif 'm' in f:
            f= float(f[:-1])*10**6
            return f
        else :
            return float(f)
        
        
    def get_followers(self):
        
        time.sleep(2)
        #open followers link of followers on any account
        # right click followers link on the page then right click on the selected script and copy selector
        flw_btn = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')))
        flw_btn.click()
        # When the pop up of followers appears webpage changes
        # so we click on follower button, then pop up appears then we click inspect , then we check the divison which get highlighted when we scroll down, copy that CSS
        popup = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.RnEpo.Yx5HN > div > div.isgrP')))
        for i in range(0,10):
            time.sleep(1)
            self.driver.e
            xecute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup) #excecuting javascripts, this tells us scroll down to the bottom of the followers list. So the scroller is at the bottom
        popup = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.RnEpo.Yx5HN > div > div.isgrP')))
        print('cool')
        b_popup = bs4(popup.get_attribute('innerHTML'),'html.parser')
        for p in b_popup.findAll('li', {'class' : 'woI9H'}):  # findAll means find all the attributes under that tag
                print(p.findAll('a')[0]['href'])  # So li tags means all the followers and 'a' tag is in that li tag to and can be used to find href of the li or followers to get to their link by savuing all href in a li
                print('Awesome')
        print('end')        
    def is_public(self):  # TO check whether account is public or private
        
        try :
            astate = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'rkEop')))
            print(astate.text)    
            if astate.text == 'This Account is Private' :
                print('try waala false')
                return False # It means its fnot public
                
            else :
                print('try waala true')
                return True
                
        except:
            print("")
            return True
        
    
    def like_post(self):
        post = self.driver.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1)')  # copy selector of the superset of the post # this is href of the first post of instagram page
        html = post.get_attribute('innerHTML') # return HTML Code of this post
        h = bs4(html,'html.parser')
        #print(h)
        href = h.a['href'] # gets it href
        self.driver.get('https://www.instagram.com'+ href) # This will get yus to the post
        #like_btn = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > svg')))
        like_btn = self.driver.find_elements_by_xpath("//button[contains(text(),'')]")[2]
        '''for i in range (0,10):
            print(str(i)+' '+like_btn[i].text)
            like_btn[i].click() # Likes the post
            time.sleep(5)
            #For finding each button what they do
        '''
        like_btn.click()
        #For unfollowing button is [0]
    
    
    def follow_page(self) :
         print("")
         self.driver.implicitly_wait(5)
         
         #follow = WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/div[2]/div/span/span[1]'))) # Follow the button
         
         follow = self.driver.find_elements_by_xpath("//button[contains(text(),'')]")[0]  # it gives list of all the buttons on the page and it works !
             
         #f_text = follow.text  # To get the text of the button
         #follow.click()
         f_text = follow.text
         print(f_text)
         if f_text.lower()  == 'follow' or f_text.lower()  == 'follow back' :
             follow.click()
             print('Started Following Account')
         else :
            print('Already following')
        
        