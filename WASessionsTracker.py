#A simple script to track someone's online sessions on WhatsApp by Neeraj Kumar.

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from playsound import playsound
from selenium.webdriver.common.keys import Keys

browser=webdriver.Chrome()
browser.get('https://web.whatsapp.com')

print("Step 1. Scan the QR Code.\nStep 2. Open up the chat for the person you want to target.\n")
target=input("Target's Name : ")
print("Running...\n")
user_status='offline'
while(True):
    soup=BeautifulSoup(browser.page_source,'html.parser')
    temp=soup.find('span',class_='O90ur')
    if str(type(temp))=="<class 'bs4.element.Tag'>":
        user_status=temp.get_text()
    if(user_status=='online' or user_status=='typing...'):
        playsound("alert.mp3")
        count=0
        print(target," is online!\n")
        localtime=time.asctime(time.localtime(time.time()))
        print("Came on : ",localtime)
        #textbox=browser.find_element_by_class_name('_2S1VP')
        #textbox.send_keys("YOUR_TEXT_HERE",Keys.ENTER)
        while(True):
            soup=BeautifulSoup(browser.page_source,'html.parser')
            temp=soup.find('span',class_='O90ur')
            if str(type(temp))!="<class 'bs4.element.Tag'>":
                user_status='offline'
                break
            count=count+1
            time.sleep(1)
        print("Session Duration: ",count," seconds\n")
        print("------------------------------------------\n")
        log = open("log.txt", "a")
        log.write("Target : "+str(target)+"\n")
        log.write("Came online on : "+str(localtime)+"\n")
        log.write("Session Duration: "+str(count)+" seconds\n")
        log.write("------------------------------------------\n")
        log.close()
        count=0

