import os #for clicky clicks
import pandas #csv/ spreadsheet stuff

#import firefox selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Firefox()

#open discord
driver.get('https://discord.com/login')

#await login
wait = WebDriverWait(driver, 120)
wait.until(EC.title_contains("Discord | Friends"))

#get sever group web element
server_list = driver.find_element(By.XPATH, "//div[@aria-label='Servers']")
servers = server_list.find_element(By.XPATH, "./child::*")

for i in servers:
    print(i)
    
#going to sleep for tonight