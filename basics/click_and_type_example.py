from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ClickAndType:

    def click_type_test(self):

        baseurl = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        login_link = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        login_link.click()

        email_field = driver.find_element(By.ID, "user_email")
        email_field.send_keys("test")

        pass_field = driver.find_element(By.ID, "user_password")
        pass_field.send_keys("test")

        time.sleep(3)
        email_field.clear()
        time.sleep(3)

        email_field.send_keys("testing")
        driver.quit()


clickandtype = ClickAndType()
clickandtype.click_type_test()


