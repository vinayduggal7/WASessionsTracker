#A simple script to track someone's online sessions on WhatsApp by Neeraj Kumar.

import time
from bs4 import BeautifulSoup
from selenium import webdriver

browser=webdriver.Chrome()
browser.get('https://web.whatsapp.com')

print("Step 1. Scan the QR Code.\nStep 2. Open up the chat for the person you want to target.\nStep 3. Press Enter.")
input()
print("Running...\n")
user_status='offline'
target='Target'
while(True):
    soup=BeautifulSoup(browser.page_source,'html.parser')
    temp=soup.find(title='online')
    if str(type(temp))=="<class 'bs4.element.Tag'>":
        user_status=temp.get_text()
    if(user_status=='online'):
        count=0
        print(target," is online!\n")
        localtime=time.asctime(time.localtime(time.time()))
        print("Came on : ",localtime) 
        while(True):
            soup=BeautifulSoup(browser.page_source,'html.parser')
            temp=soup.find(title='online')
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
        count=0

