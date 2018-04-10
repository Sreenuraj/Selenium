from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


def drag_drop():

    baseurl = "http://jqueryui.com/droppable/"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(baseurl)
    driver.implicitly_wait(5)

    driver.switch_to.frame(0)
    from_element = driver.find_element(By.ID,"draggable")
    to_element = driver.find_element(By.ID, "droppable")

    action = ActionChains(driver)
    # one way
    # action.drag_and_drop(from_element, to_element).perform()

    # another way
    action.click_and_hold(from_element).release(to_element).perform()
    time.sleep(3)

    driver.quit()


drag_drop()