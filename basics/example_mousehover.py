from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


def mouse_hover():
    baseurl = "https://learn.letskodeit.com/"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(baseurl)
    driver.implicitly_wait(10)

    practice_page = driver.find_element_by_link_text("Practice")
    practice_page.click()
    time.sleep(3)

    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(3)

    mouse_hover_ele = driver.find_element(By.ID, "mousehover")

    # to mouse hover on the button
    action = ActionChains(driver)
    action.move_to_element(mouse_hover_ele).perform()
    time.sleep(3)

    mouse_hover_action = driver.find_element(By.XPATH, "//div[@class='mouse-hover-content']//a[text()='Reload']")
    action.move_to_element(mouse_hover_action).click().perform()
    time.sleep(3)

    driver.quit()


mouse_hover()


