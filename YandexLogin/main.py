from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service('C:/chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=s)

email="testma1ltestmail@yandex.ru"
password="caramelaaa"


def first_step():
    driver.get('https://passport.yandex.ru/auth')
    driver.maximize_window()

def second_step():
    sendemail = driver.find_element_by_xpath('//*[@id="passp-field-login"]')
    sendemail.send_keys(email)

    buttonclick = driver.find_element_by_xpath('//*[@id="passp:sign-in"]')
    buttonclick.click()
    time.sleep(2)

def third_step():
    sendpass = driver.find_element_by_xpath('//*[@id="passp-field-passwd"]')
    sendpass.send_keys(password)

    enterbutton = driver.find_element_by_xpath('//*[@id="passp:sign-in"]')
    enterbutton.click()

first_step()
second_step()
third_step()