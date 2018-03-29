from selenium import webdriver
import os

class RunSafariTests():

    def test(self):

        serverLocation = "/Sreenu/Selenium/drivers/selenium-server-standalone-3.11.0.jar"
        os.environ["SELENIUM_SERVER_JAR"] = serverLocation

        # Instantiate Safari Browser Command
        driver = webdriver.Safari(quiet=True)

        # Open the provided URL
        driver.get("http://www.letskodeit.com")


safari = RunSafariTests()
safari.test()
