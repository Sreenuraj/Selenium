from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def swith_window():

    baseurl = "https://learn.letskodeit.com/"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(baseurl)
    driver.implicitly_wait(10)

    practice_page = driver.find_element_by_link_text("Practice")
    practice_page.click()

    # Find the handle for the current page
    parent_handele = driver.current_window_handle
    print(parent_handele)

    # Click on open window button
    open_window = driver.find_element(By.ID, "openwindow")
    open_window.click()

    # Find all handles
    all_handles = driver.window_handles
    for handle in all_handles:
        print(handle)

    # Switch to new window
    for handle in all_handles:
        if handle != parent_handele:
            driver.switch_to.window(handle)

    # Perform action in the new window
    search_box = driver.find_element_by_id("search-courses")
    search_box.send_keys("python")
    # click search button
    driver.find_element(By.ID, "search-course-button").click()
    time.sleep(2)
    driver.close()

    # Switch back to the parent screen
    driver.switch_to.window(parent_handele)
    driver.find_element(By.ID, "name").send_keys("testing done")


    time.sleep(3)
    driver.quit()


swith_window()