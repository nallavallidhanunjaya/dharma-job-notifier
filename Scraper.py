import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import smtplib
import schedule
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
#Load the webdriver and get the ur;4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Define the path to chromedriver
service = Service(r'C:\\Users\\nalla\\OneDrive\\Desktop\\chromedriver.exe')
url1 = "https://www.linkedin.com/jobs/search?keywords=Software%20Developer&location=Bengaluru&geoId=105214831&distance=50&f_JT=I&f_PP=105214831&f_TPR=&position=1&pageNum=0"
# Create the WebDriver instance
driver = webdriver.Chrome(service=service)

driver.implicitly_wait(10)
driver.get(url1)
from selenium.webdriver.common.by import By

y = driver.find_elements(By.CLASS_NAME, 'results-context-header__job-count')[0].text
n =pd.to_numeric(y)

# Scrolling logic
i = 2
while i <= 5:
    # for scrolling the window (automatically)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    i = i + 1
    # in case of finds the button see more jobs appears, for clicking it 
    try:
        #in case of finds the button called See more jobs
        x = driver.find_element(By.XPATH, "//button[@aria-label='See more jobs']")
        driver.execute_script("arguments[0].click();",x)
        time.sleep(3)
    # in case of doesn't find the button 
    except:
        pass
        time.sleep(4)
    
company_name= []
for j in range(n):
    try:
        company = driver.find_elements(By.CLASS_NAME,"base-search-card__subtitle")[j].text
        company_name.append(company)
    except IndexError:
        pass
title_name = [] 
for j in range(n):
    try:
        title = company = driver.find_elements(By.CLASS_NAME,"base-search-card__title")[j].text
        title_name.append(title)
    except IndexError:
        pass

link_list = []
find_link = driver.find_elements(By.CLASS_NAME,"base-card__full-link")
for k in find_link:
    link_list.append(k.get_attribute('href'))

# Creating CSV files
company_final = pd.DataFrame(company_name,columns=['Company'])
title_final = pd.DataFrame(title_name,columns=['Title'])
link_final = pd.DataFrame(link_list,columns=['Links'])
final = company_final.join([title_final,link_final])
final