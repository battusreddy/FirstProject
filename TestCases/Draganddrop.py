from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.chrome.options import Options
#     cd C:\Program Files\Google\Chrome\Application
#     chrome.exe -remote-debugging-port=9222 -user-data-dir=C:\Chomedata
opt = Options()
opt.add_experimental_option("debuggerAddress","localhost:9222")
url = "https://pynishant.github.io/"
driver = webdriver.Chrome(options=opt)
#url = "https://jqueryui.com/droppable/"
driver.get(url)
#driver.switch_to.frame(0)
actions = ActionChains(driver)
elem1 = driver.find_element_by_xpath("//*[@id='drag1']")
source1 = driver.find_element_by_xpath("//*[@id='div1']")
target1 = driver.find_element_by_xpath("//*[@id='div2']")
#actions.drag_and_drop_by_offset(source1,20,20).perform()
#actions.click_and_hold(elem1).drag_and_drop(source1,target1).release(elem1).perform()
actions.drag_and_drop(source1,target1).release().perform()
#actions.send_keys(keys.keys.ENTER).perfo
#actions.drag_and_drop(source1,target1).perform()
#actions.drag_and_drop(source1,target1).perform()



