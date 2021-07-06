from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import keys
#     cd C:\Program Files\Google\Chrome\Application
#     chrome.exe -remote-debugging-port=9222 -user-data-dir=C:\Chomedata
opt = Options()
opt.add_experimental_option("debuggerAddress","localhost:9222")
url = "https://kite.zerodha.com/dashboard"
driver = webdriver.Chrome(options=opt)
driver.get(url)
for i in range(1,130):
        i = i + 1
        n1 = ActionChains(driver)
        ideabse1 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/span[1]")
        n1.move_to_element(ideabse1).perform()
        ideabse2 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/span/span[3]/button/span")
        ideabse2.click()
        time.sleep(1)
        bserate = "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]/div[1]/div/table[1]/tbody/tr[1]/td[1]"
        time.sleep(1)
        bsevalue = driver.find_element_by_xpath(bserate).text
        print(bsevalue)
        ideabse2.click()
        ideanse1 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div/span[1]")
        n1.move_to_element(ideanse1).perform()
        ideanse2 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/span/span[3]/button/span")
        ideanse2.click()
        time.sleep(1)
        nserate = "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/table[1]/tbody/tr[1]/td[1]"
        time.sleep(1)
        nsevalue = driver.find_element_by_xpath(nserate).text
        print(nsevalue)
        ideanse2.click()
