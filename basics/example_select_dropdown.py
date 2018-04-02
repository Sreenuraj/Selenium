from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class SelectExample:

    def sel_example(self):
        baseurl = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        practice_page = driver.find_element_by_xpath("//div[@id='navbar']//a[@href='/pages/practice']")
        practice_page.click()

        dropdown = driver.find_element_by_xpath("//select[@id='carselect']")
        dropdown_sel = Select(dropdown)

        # Select by Index
        dropdown_sel.select_by_index(1)
        time.sleep(2)

        # select by Value
        dropdown_sel.select_by_value("honda")
        time.sleep(2)

        # select by Visible text
        dropdown_sel.select_by_visible_text("BMW")
        time.sleep(2)

        driver.quit()


dropdown_select = SelectExample()
dropdown_select.sel_example()