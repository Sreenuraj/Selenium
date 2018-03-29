from selenium import webdriver


class BrowserInteractions:

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()

        # Window Maximize
        driver.maximize_window()

        # Open the Url
        driver.get(baseUrl)

        # Get Title
        title = driver.title
        print("Title of the web page is:", title)

        # Get Current Url
        current_url = driver.current_url
        print("Current Url of the web page is", current_url)

        # 2 ways of Browser Refresh
        driver.refresh()
        print("Browser Refreshed 1st time")

        driver.get(driver.current_url)
        print("Browser Refreshed 2nd time")

        # Open another Url
        driver.get("https://letskodeit.teachable.com/")

        # Browser Back
        driver.back()
        print("Go one step back in browser history")

        # Browser Forward
        driver.forward()
        print("Go one step forward in browser history")

        # Get Page Source
        pageSource = driver.page_source
        #print(pageSource)
        # Browser Close / Quit
        # driver.close()
        driver.quit()


test_interactions = BrowserInteractions()
test_interactions.test()