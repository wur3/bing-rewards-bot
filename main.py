from selenium import webdriver
import time

##############################################################
#       Part 1: Loggin in
##############################################################

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
driver.find_element_by_id('idSIButton9').click()

# wait 1 second for everything to load
time.sleep(1)

# fill in input with 'password'
driver.find_element_by_id('i0118').send_keys(password)

# Submit password
driver.find_element_by_id('idSIButton9').click()

print("*hacker voice* I'm in.")
##############################################################
#       Part 2: Searching
##############################################################

# prepare list of filler search words (10 words)
with open('words.txt') as input_file:
    words = [next(input_file).rstrip() for x in range(10)]

for i in range(10):
    # wait 1 second for everything to load
    time.sleep(1)

    search_bar = driver.find_element_by_id('sb_form_q')

    #Clear old content of search bar first
    search_bar.clear()

    #Inputs content into search bar
    search_bar.send_keys(words[i])

    print("{0}. Searching \"{1}\".".format(i+1, words[i]))

    # wait 1 second for everything to load
    time.sleep(1)

    #Submits input
    driver.find_element_by_id('sb_form_go').click()
