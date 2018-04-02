from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class FindElements:

    def find_elements_to_interact(self):
        baseurl = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        practice_page = driver.find_element_by_xpath("//div[@id='navbar']//a[@href='/pages/practice']")
        practice_page.click()

        list_radio = driver.find_elements(By.XPATH, "//input[contains(@type,'radio')and contains(@name,'cars')]")
        radio_total = len(list_radio)
        print("Found {} radio button associated with cars".format(radio_total))

        for each in list_radio:
            is_selected = each.is_selected()
            if not is_selected:
                each.click()
                time.sleep(2)

        driver.quit()


find_ele = FindElements()
find_ele.find_elements_to_interact()
