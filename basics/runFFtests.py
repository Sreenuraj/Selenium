from selenium import webdriver


class RunFFtest():

    def test_ff(self):
        # Instantiate firefox
        driver = webdriver.Firefox()

        # Open the URL
        driver.get("http://www.letskodeit.com")


ff = RunFFtest()
ff.test_ff()