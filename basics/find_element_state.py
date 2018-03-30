from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class FindElementState:

    def find_state(self):

        baseurl = "https://www.google.co.in"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        element1 = driver.find_element_by_id("gs_htif0")
        element1_state = element1.is_enabled()
        print("Element1 state = ", str(element1_state))

        element2 = driver.find_element_by_id("gs_taif0")
        element2_state = element2.is_enabled()
        print("Element2 state = ", str(element2_state))

        element3 = driver.find_element_by_id("lst-ib")
        element3_state = element3.is_enabled()
        print("Element2 state = ", str(element3_state))

        element3.send_keys("Sreenuraj")
        element3.send_keys(Keys.ENTER)
        time.sleep(5)



        driver.quit()


find_state = FindElementState()
find_state.find_state()