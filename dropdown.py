from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(
    "S:\project spotify\chromedriver_win32\chromedriver.exe")
driver.get(
    "https://www.spotify.com/in-en/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F")

select = Select(driver.find_element_by_id('month'))

# select by visible text
select.select_by_visible_text('March')

# select by value 
#select.select_by_value('1')