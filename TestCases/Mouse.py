from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import keys




class testwindow:
    def testwindow1(self):
        self.url = "http://demo.automationtesting.in/Register.html"
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//a[contains(text(),'Interactions')]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//a[contains(text(),'Drag')]").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'Static')]").click()
        self.n1 = ActionChains(self.driver)
        self.n1.drag_and_drop(self.driver.find_element_by_xpath("//*[@id='mongo']"),
            self.driver.find_element_by_xpath("//*[@id='droparea']")).perform()

    def sliding(self):
        self.url = "http://demo.automationtesting.in/Slider.html"
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        self.driver.get(self.url)
        self.driver.maximize_window()
        slider = self.driver.find_element_by_xpath("//*[@id='slider']")
        self.driver.implicitly_wait(10)
        self.n1 = ActionChains(self.driver)
        self.n1.drag_and_drop_by_offset(slider,200,300).perform()
        time.sleep(30)
        self.n1.drag_and_drop_by_offset(slider,100,200).perform()

test = testwindow()
test.sliding()