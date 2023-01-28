import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

# chromeOptions = Options()
# chromeOptions.add_argument("--kiosk")


chrome_driver_path = "C:\Devellopment\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

sign_up = driver.find_element_by_xpath('/html/body/div[1]/header/nav/div/a[2]')

sign_up.click()

email = driver.find_element_by_xpath('//*[@id="username"]')
email.send_keys("antonio61231@gmail.com")
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys("Antonelo12!@")
sign_up2 = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
sign_up2.click()
time.sleep(5)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone.text == "":
    phone.send_keys("664 3676744")

#Submit the application
submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()
time.sleep(5)

clock = driver.find_element_by_xpath('//*[@id="ember357"]/span')
clock.click()