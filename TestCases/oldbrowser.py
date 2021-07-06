from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import keys
#     cd C:\Program Files\Google\Chrome\Application
#     chrome.exe -remote-debugging-port=9222 -user-data-dir=C:\Chomedata
opt = Options()
opt.add_experimental_option("debuggerAddress","localhost:9222")
url = "http://demo.automationtesting.in/Vimeo.html"
driver = webdriver.Chrome(options=opt)
driver.get(url)
driver.switch_to_frame(driver.find_element_by_xpath("//*[@id='foo']"))
driver.implicitly_wait(10)
driver.
driver.find_element_by_xpath("//*[@id='player']/div[7]/div[3]/button").click()
