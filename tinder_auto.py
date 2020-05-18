import subprocess
import sys
import random
#checking if selenium is present in your system
try:
    from selenium import webdriver
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'selenium'])
finally:
    from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from  selenium.common.exceptions import NoSuchElementException


#login in with your gmail account
def login(account,password):
    #opens tinder website
    i=0
    while i==0:
        driver=webdriver.Chrome(executable_path="chromedriver.exe") #chrome driver for windows change this as per your OS
        driver.implicitly_wait(5)
        driver.get("https://tinder.com/")
        print("opening tinder website")
        time.sleep(5)
        print("Clicking on cookies")
        cookies=driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()
        print("finding Google account Xpath")
        x=driver.find_elements_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div/div/button')
        if(len(x)==1):
            i=1
        else:
            print("quitting and opening again")
            print()
            driver.quit()
            time.sleep(3)
    time.sleep(5)
    print("Clicking on google login")
    driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div/div/button').click()
    #switching between main window to login window
    time.sleep(5)
    print("switching between windows")
    windows=driver.window_handles
    driver.switch_to.window(windows[1])
    
    #finding login fields and logging into your account
    print("logging in to your account")
    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(account)
    driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
    driver.switch_to.window(windows[0])
    
    #enabling location and disabling notifications
    time.sleep(3)
    print("Enabling location and disabling notifications")
    driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
    driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]').click()
    print("logged in successfully")
    return driver

def like_dislike(x,driver):
    i=0
    time.sleep(3)
    print("In like_dislike function function")
    print("displays name of person when liked:")
    while(i<x):
        time.sleep(random.random()*2)
        
        #checking for any popup
        try :
            driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]').click() #checking for popups
            print("got popup")
        
        #if there is no popup bot taps like or dislike function
        except:  
           j=0
           number=random.random()  #using for random dislike and like
           tap=random.randint(1,9) #changing pictures of profile
           while (tap>j):
                driver.find_element_by_xpath('//*[@id="Tinder"]/body').send_keys(Keys.SPACE) #taping on images
                time.sleep(random.randint(2,3))
                j=j+1
           if number>.50: #clicks on like button
                print("like:",end=" ")
                print("name:",driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/div/div[1]/div/div').text)   
                driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').click()
           else: #click on dislike button
                print("dislike:",end=" ")
                print("name:",driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/div/div[1]/div/div').text)   
                driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button').click()
        i=i+1
            
#give your google account details.
driver=login()

 #number of likes you want to perform
n=10
like_dislike(n,driver)