from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]


chrome_driver_path = "/Users/david.cordero/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.speedtest.net/")
start_button = driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a")
start_button.click()

time.sleep(45)
download_speed = driver.find_element_by_class_name("download-speed")
upload_speed = driver.find_element_by_class_name("upload-speed")



if float(download_speed.text) > 50.0 or float(upload_speed) > 0.1:
    driver.get("https://twitter.com/login")
    time.sleep(2)
    username = driver.find_element_by_name("session[username_or_email]")
    password = driver.find_element_by_name("session[password]")
    username.send_keys(EMAIL)
    password.send_keys(PASSWORD)
    password.send_keys(Keys.ENTER)
    time.sleep(1)
    tweet_box = driver.find_element_by_class_name("public-DraftStyleDefault-ltr")
    tweet_box.send_keys("Input text here")
    send_tweet = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/"
                                              "div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div")
    send_tweet.click()

driver.quit()