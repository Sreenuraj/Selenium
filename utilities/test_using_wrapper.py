from selenium import webdriver
from utilities.wrapper import Wrapper
import time


class TestWrapper:

    def test(self):
        baseurl = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        wrapper = Wrapper(driver)
        driver.get(baseurl)
        driver.implicitly_wait(10)

        practice_page = wrapper.get_element("//div[@id='navbar']//a[@href='/pages/practice']", 'xpath')
        practice_page.click()

        textfield1 = wrapper.get_element("name")
        textfield1.send_keys("testing")
        time.sleep(3)

        textfield2 = wrapper.get_element("//input[@id='name']", 'xpath')
        textfield2.clear()
        time.sleep(3)

        textfield3 = wrapper.is_element_present("name", 'id')
        print("state of the element is :", str(textfield3))

        textfield4 = wrapper.is_element_present("//input[@id='name1']", 'xpath')
        print("state of the element is :", str(textfield4))

        driver.quit()


test_wrapper = TestWrapper()
test_wrapper.test()

