from selenium import webdriver
# pytest -v -s TestCases/Testlocators.py

class testloc:

    def testid(self):
        header = True
        self.url="https://htmlcolorcodes.com/color-names/"
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        self.driver.get(self.url)
        self.driver.maximize_window()
        total = 0
        noofsections = len(self.driver.find_elements_by_xpath("//*[@id='names']/section"))
        print(f"Total no of sections  -- {noofsections}")
        for s in range (1,noofsections):
            print(f"Section name is -- {s}")
            noofrows = len(self.driver.find_elements_by_xpath("//*[@id='names']/section["+str(s)+"]/div/table/tbody/tr"))
            print(f'total no od rows are -- {noofrows}')
            i = 0
            for i in range(1,noofrows+1):
                color = self.driver.find_element_by_xpath("//*[@id='names']/section["+str(s)+"]/div/table/tbody/tr["+str(i)+"]/td[2]").text
                hex = self.driver.find_element_by_xpath("//*[@id='names']/section["+str(s)+"]/div/table/tbody/tr["+str(i)+"]/td[3]").text
                if header == True:
                    print("Color -- " , "      ", "Hex Value --")
                    header = False
                print(color,"     ", hex)
                total = total + 1
        self.driver.close()
        print(f'Total rows are {total}')
mytest1 = testloc   ()
mytest1.testid()