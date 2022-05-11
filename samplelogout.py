

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

#ramdevgwo@gmail.com

driver_path = "S:\project spotify\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(driver_path)
login_link="https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F"

def signout(email,password):
    #login
    driver.get(login_link)
    email_block = driver.find_element_by_id("login-username")
    password_block = driver.find_element_by_id("login-password")
    
    email_block.send_keys(email)
    password_block.send_keys(password)
    
    
    #//*[@id="login-button"]
    
    time.sleep(10)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="login-button"]'))).click()
    
    my_channel = "https://open.spotify.com/user/dcxuy5q4jfrkyrgrq8v3xencg"
    time.sleep(10)
    driver.get(my_channel)
    
    #//*[@id="main"]/div/div[2]/div[1]/header/button/figure/div/div
    time.sleep(10)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/header/button/figure/div/div'))).click()
    
    #//*[@id="context-menu"]/div/ul/li[4]/button
    
    time.sleep(10)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="context-menu"]/div/ul/li[4]/button'))).click()
    
email="ramdevgwo@gmail.com"
password="ratQ129#2!@"

signout(email,password)