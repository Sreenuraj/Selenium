from selenium.webdriver.common.by import By


class Wrapper:

    def __init__(self, driver):
        self.driver = driver

    def get_bytype(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == 'id':
            return By.ID
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "classname":
            return By.CLASS_NAME
        elif locator_type == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type not supported")

    def get_element(self, locator, locator_type='id'):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_bytype(locator_type)
            element = self.driver.find_element(by_type, locator)
        except:
            print("Not Supported")
        return element

    def is_element_present(self, locator, locator_type):
        locator_type = locator_type.lower()
        by_type = self.get_bytype(locator_type)
        try:
            element = self.driver.find_elements(by_type, locator)
            if len(element)>0:
                print("Element is present")
                return True
            else:
                print("Element not Found")
                return False
        except:
            print("Something went wrong")
