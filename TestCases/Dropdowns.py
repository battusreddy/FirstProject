from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import keys




url = "http://demo.automationtesting.in/Register.html"
driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.implicitly_wait(5)
driver.get(url)
driver.maximize_window()
Select(driver.find_element_by_xpath("//*[@id='Skills']")).select_by_value("Python")


