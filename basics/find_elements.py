from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElements:

    def test(self):
        baseurl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseurl)

        elements_withclass = driver.find_elements_by_class_name("inputs")
        length_elements_withclass = len(elements_withclass)

        print("Found {} elements with class name 'input'".format(length_elements_withclass))

        elements_withtag = driver.find_elements(By.TAG_NAME, "h1")
        length_elements_withtag = len(elements_withtag)

        print("Found {} elements with tag name".format(length_elements_withtag))


elements = FindElements()
elements.test()
