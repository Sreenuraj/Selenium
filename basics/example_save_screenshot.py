from selenium import webdriver
from selenium.webdriver.common.by import By


def take_screenshot():
    baseurl = "https://letskodeit.teachable.com/"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(baseurl)
    driver.implicitly_wait(5)

    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element_by_id("user_email").send_keys("aaa@aaa.com")
    driver.find_element_by_id("user_password").send_keys("dddd")
    driver.find_element_by_xpath("//input[@type='submit']").click()

    dir_screenshot = "/Users/lz69/Downloads/test.png"

    try:
        driver.save_screenshot(dir_screenshot)
        print("Screenshot saved")
    except NotADirectoryError:
        print("dir not found")

    driver.quit()


take_screenshot()

