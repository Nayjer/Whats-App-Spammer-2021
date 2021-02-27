from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options) 
driver.get('https://web.whatsapp.com/')

name = "Micha" #type here the name of the contact in
msg = "test" #message to send
count = 2 #number of repetitions

input('Enter anything after scanning QR code') #you need to press enter in your terminal, after you scan the QR-Code with your phone

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)) #here it finds the user
user.click()
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]' #finds the chat box where we ususally type messages in
input_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
for i in range(count): 
    input_box.send_keys(msg + Keys.ENTER) #sends the message(s)
