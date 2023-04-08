import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome("c:/Users/festu/OneDrive/Documents/chromedriver.exe")
driver.get("https://tinder.com/")
time.sleep(5)
login =driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]")
login.click()
time.sleep(8)
google = driver.find_element(By.XPATH, value="/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div/div")
google.click()
time.sleep(8)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
username = driver.find_element(By.XPATH, value='/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
username.send_keys(os.environ.get("username"))
password = driver.find_element(By.XPATH, value="/html/body/div/div[2]/div[1]/form/div/div[2]/div/input")
password.send_keys(os.environ.get("password"))
next_b = driver.find_element(By.XPATH, value="/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input")
next_b.click()
time.sleep(20)
driver.switch_to.window(base_window)

allow = driver.find_element(By.XPATH,value="/html/body/div[2]/main/div/div/div/div[3]/button[1]")
allow.click()
time.sleep(1)
allow = driver.find_element(By.XPATH,value="/html/body/div[2]/main/div/div/div/div[3]/button[1]")
allow.click()
allow = driver.find_element(By.XPATH,value="/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button")
allow.click()
time.sleep(20)
like = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button/span/span")
for x in range(100):
    try:
        time.sleep(30)
        like.click()
    except NoSuchElementException:
        x = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[1]/div/main/div[2]/main/div/div[1]/div/div[4]/button")
        x.click()


driver.quit()