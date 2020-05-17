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
        driver.implicitly_wait(10)
        driver.get("https://tinder.com/")
        time.sleep(5)
        cookies=driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()
        x=driver.find_elements_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div/div/button')
        if(len(x)==1):
            i=1
        else:
            driver.quit()
            time.sleep(3)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div/div/button').click()
    #switching between main window to login window
    time.sleep(5)
    windows=driver.window_handles
    driver.switch_to.window(windows[1])
    
    #finding login fields and logging into your account
    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(account)
    driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
    driver.switch_to.window(windows[0])
    
    #enabling location and disabling notifications
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
    driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]').click()
    return driver

def like_dislike(x,driver):
    i=0
    while(i<x):
        number=random.random()
        time.sleep(random.random()*10)
        j=0
        tap=random.randint(0, 10)
        while (tap>j):
            driver.find_element_by_xpath('//*[@id="Tinder"]/body').send_keys(Keys.SPACE)
            time.sleep(random.randint(1,4))
            j=j+1
        try:
            driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]').click()
        except:
            if number>.50:
                print("name:",driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/div/div[1]/div/div').text)
                driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').click()
                print("like")
            else:
                print("dislike")
                driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button').click()
            i=i+1
        
#give your google account details.
driver=login()
#number of iterations you want to do
n=10 #number of likes you want to perform
like_dislike(n,driver)