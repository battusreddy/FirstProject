from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains
opt = Options()
opt.add_experimental_option("debuggerAddress","localhost:9222")
url = "https://iii3.lightning.force.com/lightning/page/home"
driver = webdriver.Chrome(options=opt)
driver.get(url)
driver.implicitly_wait(10)
ele1 = "//body/div[4]/div[1]/section[1]/div[1]/div[1]/one-appnav[1]/div[1]/one-app-nav-bar[1]/nav[1]/div[1]/one-app-nav-bar-item-root[2]"
driver.find_element_by_xpath(ele1).click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//body/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/a[1]").click()
driver.implicitly_wait(5)
driver.switch_to_active_element()
driver.implicitly_wait(5)
#driver.find_element_by_xpath("/html[1]/body[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/article[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("Suresh1")
driver.find_element_by_xpath("//div/label/span[text()='Account Name']/following::input[1]").send_keys("MAGICs1")
driver.find_element_by_xpath("//div/label/span[text()='Account Name']/following::input[2]").send_keys("Parent")
driver.find_element_by_xpath("//div/label/span[text()='Account Name']/following::input[3]").send_keys("WEBSITE")
driver.find_element_by_xpath("//div/label/span[text()='Account Name']/following::input[4]").send_keys("99000000")
driver.find_element_by_xpath("//div/label/span[text()='Account Name']/following::input[5]").send_keys("22")
driver.find_element_by_xpath("//body/div[4]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[3]").click()