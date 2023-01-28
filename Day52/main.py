import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "C:\Devellopment\chromedriver.exe"
INSTAGRAM_EMAIL = "antonio61231@gmail.com"
INSTAGRAM_PASSWORD = "Antonelo12!@"
FOLLOW_URL = 'https://www.instagram.com/cristiano/'
LOGIN_URL = 'https://www.instagram.com/'


class InstaFollower():

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get(LOGIN_URL)
        time.sleep(3)
        email = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        email.send_keys(INSTAGRAM_EMAIL)
        password = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        password.send_keys(INSTAGRAM_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(10)

    def find_followers(self):
        self.driver.get(FOLLOW_URL)
        followers = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(5)
        dialog = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        # find number of followers
        # scroll down the page
        for i in range(1,11):
            self.follow(i)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
            time.sleep(random.randint(1500, 2000) / 1000)

    def follow(self,button_number):
        buttons = self.driver.find_elements_by_css_selector(".PZuss li div div button")
        for i in range(6*button_number):
            try:
                buttons[i].click()
                time.sleep(3)
            except:
                cancel = self.driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[2]")
                cancel.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
