import time

from selenium import webdriver
from selenium.webdriver.common import keys

chrome_driver_path = "C:\Devellopment\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com/app/recs")

time.sleep(2)
sesion = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
sesion.click()
time.sleep(2)
facebook = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook.click()
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
time.sleep(2)
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys("pucca51231@gmail.com")
password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys("antonelo12!@")
password.send_keys(keys.Keys.ENTER)
driver.switch_to.window(base_window)
print(driver.title)
time.sleep(5)
location = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/button[1]")
location.click()
no_accepto = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]')
no_accepto.click()
cookies = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button')
cookies.click()
time.sleep(10)
like = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
while True:
   try:
       like.click()
       time.sleep(2)
   except:
      try:
          no_accepto2 = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]')
          no_accepto2.click()
      except:
         pass

