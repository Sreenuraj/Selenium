from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


def slider():

    baseurl = 'http://jqueryui.com/slider/'
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseurl)

    driver.switch_to.frame(0)
    action = ActionChains(driver)

    slider_element = driver.find_element(By.XPATH, "//div[@id='slider']//span")
    # below for dragging the slider
    action.drag_and_drop_by_offset(slider_element, 200, 0).perform()
    time.sleep(3)

    driver.quit()


slider()
