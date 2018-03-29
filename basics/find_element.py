from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElements():

    def test_to_findElements(self):
        testurl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(testurl)

        ele_id = driver.find_element_by_id("name")
        ele_name = driver.find_element_by_name("show-hide")

        if ele_id is not None and ele_name is not None:
            print("Found ID and Name")

        ele_xpath = driver.find_element_by_xpath("//input[@id='name']")
        ele_css = driver.find_element_by_css_selector("#displayed-text")

        if ele_xpath is not None and ele_css is not None:
            print("Found xpath and css")

        ele_linktext = driver.find_element_by_link_text("Login")
        ele_par_linktext = driver.find_element_by_partial_link_text("Prac")

        if ele_linktext is not None and ele_par_linktext is not None:
            print("Found linktext and partialLinktext")

        by_ele_xpath  = driver.find_element(By.XPATH, "//input[@id='name']")
        if by_ele_xpath is not None:
            print("Found xpath")



element = FindElements()
element.test_to_findElements()