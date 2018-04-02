from selenium import webdriver


class TextValue:

    def find_text_value(self):
        baseurl = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        practice_page = driver.find_element_by_xpath("//div[@id='navbar']//a[@href='/pages/practice']")
        practice_page.click()

        text_tofind = driver.find_element_by_id("opentab")
        print("The text is : ", text_tofind.text)

        value_tofind = driver.find_element_by_id("name")
        print("The value of the attribute class is : ", value_tofind.get_attribute("class"))

        driver.quit()


ff = TextValue()
ff.find_text_value()