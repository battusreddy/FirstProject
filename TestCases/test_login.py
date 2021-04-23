import pytest

from selenium import webdriver
from PageObject.LoginPage import LoginPage
from Utilities.readProperties import readconfig
from Utilities.customlogger import LogGen
# pytest -v -s TestCases/test_login.py
# pytest -v -s TestCases/test_login.py --browser chrome
# pytest -v -s -n=2 TestCases/test_login.py --browser chrome
# pytest -v -s --html=Reports\report.html TestCases/test_login.py --browser chrome
# pytest -v -s -m "Sanity or Regression" TestCases/test_login.py --browser chrome
class Testlogin001:
    baseURL = readconfig.getapplicationURL()
    username = readconfig.getusername()
    password = readconfig.getpassword()

    logger = LogGen.loggen()

    @pytest.mark.Sanity
    def testlogin1(self,setup):
        self.logger.info("Test case 001 - Homepage Title Started--------")
        self.driver = setup
        #self.driver = webdriver.Chrome('C:/Users/battu/Downloads/chromedriver_win32/chromedriver.exe')
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        acttitle = self.driver.title
        if acttitle == "Dashboard / nopCommerce administration":
            self.driver.save_screenshot(".\\ScreenShots\\" + "Pass_" + "homepage.png")
            self.logger.info("Test case - Homepage Title test Passed--------")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "Fail_" + "homepage.png")
            self.logger.info("Test case - Homepage Title test Failed--------")
            self.driver.close()
            assert False

    @pytest.mark.Regression
    def testlogin2(self,setup):
        self.logger.info("Test case 002- Homepage Title Started--------")
        self.driver = setup
        #self.driver = webdriver.Chrome('C:/Users/battu/Downloads/chromedriver_win32/chromedriver.exe')
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        acttitle = self.driver.title
        if acttitle == "Dashboard / nopCommerce administratio":
            self.driver.save_screenshot(".\\ScreenShots\\" + "Pass_" + "homepage.png")
            self.logger.info("Test case - Homepage Title test Passed--------")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "Fail_" + "homepage.png")
            self.logger.info("Test case - Homepage Title test Failed--------")
            self.driver.close()
            assert False