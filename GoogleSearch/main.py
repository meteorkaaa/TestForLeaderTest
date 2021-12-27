from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service('C:/chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=s)

def start():
    driver.get("https://google.com")
    driver.maximize_window()

def get_result():
    founder = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input')
    founder.send_keys(" купить кофемашину bork c804 source:mvideo.ru OR купить кофемашину bork c804")
    foundbutton = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
    foundbutton.click()

start()
get_result()