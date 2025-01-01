from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.support import expected_conditions as EC
import time  
import os
from dotenv import load_dotenv

load_dotenv()

driver = webdriver.Chrome()

try:
    driver.get("http://www.google.com")
    time.sleep(1)
    search_box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
    search_box.send_keys("LinkedIn") 
    search_box.submit()  
    time.sleep(5)
    
    linked_in = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[12]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/div[1]/div/span/a/h3')
    linked_in.click()
    time.sleep(2)
    
    sign_in = driver.find_element(By.XPATH, '/html/body/nav/div/a[2]')
    sign_in.click()
    time.sleep(3)
    
    email = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[1]/input')
    email.send_keys("johnabhraham286@gmail.com")
    time.sleep(4)
    
    password = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[2]/input')
    pass_key = os.getenv("PASSWORD")
    password.send_keys(pass_key)
    time.sleep(6)
    
    sign_in_button = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[4]/button')
    sign_in_button.click()
    time.sleep(5)
    
    jobs = driver.find_element(By.XPATH, '/html/body/div[6]/header/div/nav/ul/li[3]/a')
    jobs.click()
    time.sleep(3)
    
    search_box = driver.find_element(By.XPATH, '/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]')
    search_box.send_keys("Data Engineer Intern")
    time.sleep(3)
    
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)
    all_filters = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/div/div/button')
    all_filters.click()
    time.sleep(3)
    most_recent = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/ul/li[2]/fieldset/div/ul/li[1]/label/p/span[1]')
    most_recent.click()
    time.sleep(3)
    past_24_hours = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/ul/li[3]/fieldset/div/ul/li[4]/label/p/span[1]')
    past_24_hours.click()
    time.sleep(3)
    intern = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/ul/li[4]/fieldset/div/ul/li[1]/label/p/span[1]')
    intern.click()
    time.sleep(3)
    easy_apply = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/ul/li[8]/fieldset/div/div')
    easy_apply.click()
    time.sleep(3)
    submit = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[3]/div/button[2]/span')
    submit.click()


    time.sleep(3000)

finally:
    # Close the browser
    driver.quit()
