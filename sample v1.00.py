from select import select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import data as people_data
import random as random
import time
import pandas as pd
#============================================================================
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#important links


csv_file = ""
driver_path = "S:\project spotify\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(driver_path)

def signup(email,password,name):
    signuplink = "https://www.spotify.com/in-en/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F"
    driver.get(signuplink)
   
    month_lis = ["January", "March", "May", "July",
                 "August", "October", "November", "December"]
    
    genders = ['//*[@id = "__next"]/main/div/div/form/fieldset/div/div[1]/label',
               '//*[@id = "__next"]/main/div/div/form/fieldset/div/div[2]/label']
    year=random.randint(1990,2004)
    day=random.randint(1,31)
    month=random.choice(month_lis)
    gender=random.choice(genders)
    #finding the blocks
    email_block = driver.find_element_by_id("email")
    confirm_email_block=driver.find_element_by_id("confirm")
    password_block = driver.find_element_by_id("password")
    displayname_block=driver.find_element_by_id("displayname")
    year_block=driver.find_element_by_id("year")
    #month dropdown
    month_block = Select(driver.find_element_by_id('month'))
    day_block=driver.find_element_by_id("day")
    #gender_block=driver.find_element_by_id(gender)
        
    #filling the data
    email_block.send_keys(email)
    confirm_email_block.send_keys(email)
    password_block.send_keys(password)
    displayname_block.send_keys(name)
    year_block.send_keys(year)
    # select by visible text
    month_block.select_by_visible_text(month) 
    day_block.send_keys(day)
    #gender_block.click()
    time.sleep(15)
    #driver.find_element_by_xpath('/html/body/div[1]/main/div/div/form/fieldset/div/div[1]/input').click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,gender ))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/main/div/div/form/div[6]/div/label '))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/main/div/div/form/div[7]/div/label  '))).click()
    time.sleep(10)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/main/div/div/form/div[9]/div/button/div[1]  '))).click()
    
    my_channel = "https://open.spotify.com/user/dcxuy5q4jfrkyrgrq8v3xencg"
    time.sleep(7)
    driver.get(my_channel)
    #//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[3]/div/button[1]
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[3]/div/button[1]  '))).click()
    time.sleep(3)
    
    #logout 
    time.sleep(10)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/button/figure/div/div'))).click()

    #//*[@id="context-menu"]/div/ul/li[4]/button

    time.sleep(10)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="context-menu"]/div/ul/li[4]/button'))).click()



name = "ramdev"+random.choice(list(map(chr, range(97, 123)))) + \
    random.choice(list(map(chr, range(97, 123)))) + \
    random.choice(list(map(chr, range(97, 123))))
domain = "@gmail.com"
email = name+domain
print(email)
signup(email,"ratQ129#2!@","Ram dev")

"""
for data in people_data:
    name=data[0]
    email=data[1]
    password=data[2]
    
    print(data)
    
    try:
        signup(email, password, name)
        
    except :
        driver.close()
        continue


"""
