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

#set wait driver time as 120 secconds
wait = WebDriverWait(driver, 120)

os.system('clear') #clear scrn
print('You have 2 MINUTES to login to Discord.')
print('*** Use the QR code to login easily ***')

#initiate wait
wait.until(EC.title_contains("Discord | Friends"))


#get sever group web element
server_list = driver.find_element(By.XPATH, "//div[@aria-label='Servers']")
servers = server_list.find_elements(By.CLASS_NAME, "blobContainer-ikKyFs")


print("SELECT A SERVER BELOW")
print("---------------------")
print_ser = 0
while print_ser-1 != servers.__len__:
    print(print_ser, '. ', servers[print_ser-1].get_attribute("data-dnd-name"))
    print_ser = print_ser + 1


#going to sleep for tonight