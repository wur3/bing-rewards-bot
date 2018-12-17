from selenium import webdriver

username = ''
password = ''

url = 'https://www.bing.com/'

driver = webdriver.Chrome("/home/rich3u/Downloads/chromedriver")

driver.get(url)
