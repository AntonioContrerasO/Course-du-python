from selenium import webdriver
from datetime import datetime
import time

chrome_driver_path = "C:\Devellopment\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_xpath('//*[@id="cookie"]')
five_min = time.time() + 60*5 # 5minutes


while True:
    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()
    money = int(driver.find_element_by_xpath('//*[@id="money"]').text)
    panels = driver.find_elements_by_css_selector("#store div")
    if datetime.now().second % 5 == 0:
        for i in range(7,-1,-1):
            try:
                if money >= int(panels[i].text.split(" -")[1].split("\n")[0].strip().replace(",", "")):
                    panels[i].click()
                    continue
            except:
                pass
    print(time.time())
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break


