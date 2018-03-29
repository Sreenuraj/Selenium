from selenium import webdriver


class RunChromeTest():

    def run_test(self):

        # instantiate the driver
        driver = webdriver.Chrome()

        # open the url
        driver.get("http://www.letskodeit.com")


chrome_test = RunChromeTest()
chrome_test.run_test()