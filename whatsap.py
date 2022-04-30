from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from config import CHROME_DATA_PATH
import os

os.system("taskkill /im chrome.exe /f")
options = webdriver.ChromeOptions()
options.add_argument(CHROME_DATA_PATH)

driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)

driver.get('https://web.whatsapp.com')
time.sleep(15)



def send_message(mobile_no, message):
    search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search_box.send_keys(mobile_no)
    time.sleep(2)
    
    driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]').click()
    time.sleep(2)
    
    message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    message_box.send_keys(message)
    #enable enter key in the whatsapp>setting>chat on phone
    message_box.send_keys(Keys.ENTER)
    print('"'+message+'" send to '+mobile_no)
    
mobile_no = "" #mobile no. of the person you want to send message
send_message(mobile_no, "testing")
    