from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def iframe_switch():
    baseurl = "https://learn.letskodeit.com/"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(baseurl)
    driver.implicitly_wait(10)

    practice_page = driver.find_element_by_link_text("Practice")
    practice_page.click()
    element = driver.find_element(By.ID, "courses-iframe")
    element.location_once_scrolled_into_view
    time.sleep(3)

    # Switch to iframe using ID by giving the ID of the frame as argument
    #driver.switch_to.frame("courses-iframe")

    # Switch to iframe using name by giving the name of the frame as argument
    #driver.switch_to.frame("iframe-name")

    # Switch to iframe using the number(which ifrome in the page to click, here 0)
    driver.switch_to.frame(0)

    # Perform some action in the frame window
    driver.find_element(By.ID, "search-courses").send_keys("python")
    time.sleep(3)

    # Switch back to main window
    driver.switch_to.default_content()
    driver.execute_script("window.scrollBy(0, -1000);")
    time.sleep(3)
    driver.find_element(By.ID, "name").send_keys("testing done")
    time.sleep(3)

    driver.quit()


iframe_switch()
