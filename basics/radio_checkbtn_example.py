from selenium import webdriver
import time


class RadioandCheck:

    def radio_check(self):

        baseurl = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        practice_page = driver.find_element_by_xpath("//div[@id='navbar']//a[@href='/pages/practice']")
        practice_page.click()

        bmw_radio = driver.find_element_by_id("bmwradio")
        bmw_radio.click()
        time.sleep(3)

        benz_radio = driver.find_element_by_id("benzradio")
        benz_radio.click()
        time.sleep(3)

        bmw_check = driver.find_element_by_id("bmwcheck")
        bmw_check.click()
        time.sleep(3)

        benz_check = driver.find_element_by_id("benzcheck")
        benz_check.click()
        time.sleep(3)

        print("Is bmw_radio selected?" , str(bmw_radio.is_selected()))
        print("Is benz_radio selected?", str(benz_radio.is_selected()))
        print("Is bmw_check selected?", str(bmw_check.is_selected()))
        print("Is benz_check selected?", str(benz_check.is_selected()))

        driver.quit()


radio_check = RadioandCheck()
radio_check.radio_check()
