# -------------------------------------------------------
# Developed by Maddy Rai & Amandeep Gangwar
# April 15 2021
# Only for academic use
# -------------------------------------------------------


import sys
from selenium import webdriver
import time


# -------------------------------------------------------
# driver.find_element_by_link_text('abcd') works only for tags within <a> ... </a>

# if chromedriver is not in your path, you’ll need to add it here
# (https://stackoverflow.com/questions/29858752/error-message-chromedriver-executable-needs-to-be-available-in-the-path)

# Ensure Chromedriver binary matches your current Chrome version
# C:\Program Files (x86)\Google\Chrome\Application\chromedriver_win32
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# -------------------------------------------------------


class webscraper_etf_holdings:
    # instance attributes
    def __init__(self, website, fpath):
        self.website = website
        self.fpath = fpath

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    # instance method
    def simple_fetch(self):
        chromeopt = webdriver.ChromeOptions()
        prefs = {"download.default_directory": self.fpath}
        chromeopt.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=chromeopt)

        print("Connecting to website: " + self.website)

        # Enter the URL and pause for the website to load (file will download)
        try:
            # No handling of an invalid URL here as title is not matched (URL directly downloads file)
            driver.get(self.website)
            time.sleep(2)
            driver.close()
            driver.quit()

        except Exception:
            driver.close()
            driver.quit()
            print("Unexpected error:", sys.exc_info()[0])
            raise


dirdownload = r"C:\Users\????\FolderYouWant???\\"

URL = "https://www.ssga.com/library-content/products/fund-data/etfs/us/holdings-daily-us-en-spy.xlsx"
obj4 = webscraper_etf_holdings(URL, dirdownload)
obj4.simple_fetch()

URL = "https://www.invesco.com/us/financial-products/etfs/holdings/main/holdings/0?audienceType=Investor&action=download&ticker=QQQ"
obj5 = webscraper_etf_holdings(URL, dirdownload)
obj5.simple_fetch()
