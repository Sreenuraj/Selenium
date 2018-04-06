from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def handle_alert():
    baseurl = "https://learn.letskodeit.com/"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(baseurl)
    driver.implicitly_wait(10)

    practice_page = driver.find_element_by_link_text("Practice")
    practice_page.click()

    text_box = driver.find_element(By.ID, "name")
    text_box.send_keys("Sreenuraj")
    time.sleep(3)

    alert_btn = driver.find_element(By.ID, "alertbtn")
    alert_btn.click()
    time.sleep(3)

    # To perform action in alert button
    alert = driver.switch_to.alert
    alert.accept()  # click ok
    time.sleep(3)

    text_box.send_keys("Sreenuraj")
    cnfrm_btn = driver.find_element(By.ID, "confirmbtn")
    cnfrm_btn.click()
    time.sleep(3)

    # To perform action in the confirm alert, treated as alert
    alert = driver.switch_to.alert
    alert.dismiss()  # clicks cancel
    time.sleep(3)

    driver.quit()


handle_alert()

