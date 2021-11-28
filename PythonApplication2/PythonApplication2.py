from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()

driver.get('https://netpeak.ua/')

select = driver.find_element_by_xpath('//*[@id="rec278727844"]/div/div/div/div[1]/div/nav/div[1]/div[1]/ul/li[3]')
select.click()

select.dropDown.select.By.VisibleText("team")
select.click()