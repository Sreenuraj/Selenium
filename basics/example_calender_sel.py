from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DateSelect:

    def select_date(self):
        baseurl = "https://www.expedia.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(5)

        flights_tab = driver.find_element(By.XPATH, "//button[@id='tab-flight-tab-hp']")
        flights_tab.click()

        cal_dep = driver.find_element_by_xpath("//input[@id='flight-departing-hp-flight']")
        cal_dep.click()

        sel_date_27 = driver.find_element_by_xpath(
            "//button[@class='datepicker-cal-date'][contains(@data-day, '27')and contains(@data-month, '3')]")
        sel_date_27.click()

        time.sleep(3)

        driver.quit()

test_sel_date = DateSelect()
test_sel_date.select_date()