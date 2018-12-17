from selenium import webdriver
import time

# username and password are read from the first two lines of login.txt
with open('./login.txt') as input_file:
    username = next(input_file).rstrip()
    password = next(input_file).rstrip()

url = 'https://www.bing.com/'

driver = webdriver.Chrome("/home/rich3u/Downloads/chromedriver")

browser = driver.get(url)

# wait 1 second for everything to load
time.sleep(1)

# Redirects to login page
driver.find_element_by_id('id_s').click()

# wait 1 second for everything to load
time.sleep(1)

# fill in input with 'username'
driver.find_element_by_id('i0116').send_keys(username)

# Submit username/email/phone number
driver.find_element_by_id("idSIButton9").click()

# wait 1 second for everything to load
time.sleep(1)

# fill in input with 'password'
driver.find_element_by_id('i0118').send_keys(password)

# Submit password
driver.find_element_by_id("idSIButton9").click()
