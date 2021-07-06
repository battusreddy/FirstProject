from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import keys




class testwindow:
    def testwindow1(self):
        self.url = "http://demo.automationtesting.in/Alerts.html"
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        self.driver.get(self.url)
        self.driver.maximize_window()
      #  self.driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//button[contains(text(),'alert box:')]").click()
        self.n1 = self.driver.switch_to_alert()
        self.n1.accept()

    def testwindow2(self):
        self.url = "http://demo.automationtesting.in/Alerts.html"
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//a[contains(text(),'Alert with Textbox')]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//button[contains(text(),'click the button to demonstrate the prompt box')]").click()
        self.n1 = self.driver.switch_to_alert()
        self.n1.send_keys("Suresh B")
        self.n1.accept()

    def testwindow3(self):
        self.url = "http://demo.automationtesting.in/Register.html"
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//a[contains(text(),'Interactions')]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//a[contains(text(),'Selectable')]").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'Serialize')]").click()
        self.multisel = ActionChains(self.driver)
        self.multisel.key_down(keys.Keys.CONTROL).perform()
        self.driver.find_element_by_xpath("//*[@id='Serialize']/ul/li[2]/b").click()
        self.driver.find_element_by_xpath("//*[@id='Serialize']/ul/li[6]/b").click()
        self.multisel.key_up(keys.Keys.CONTROL).perform()
        results = self.driver.find_element_by_xpath("//span[@id='result']").text
        print(results)

    def testwindow4(self):
        self.url = "http://demo.automationtesting.in/Register.html"
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//a[contains(text(),'Widgets')]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//a[contains(text(),'Datepicker')]").click()
        self.driver.find_elements_by_xpath("//input[@id='datepicker2']").clear()
        self.driver.find_element_by_xpath("//input[@id='datepicker2']").send_keys("03092021")
        self.driver.find_element_by_xpath("//img[@class='imgdp']").click()




test = testwindow()
test.testwindow1()