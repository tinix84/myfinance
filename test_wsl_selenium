import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

def execute_with_retry(method, max_attempts):
    e = None
    for i in range(0, max_attempts):
        try:
            return method()
        except Exception as e:
            print(e)
            time.sleep(1)
    if e is not None:
        raise e

capabilities = DesiredCapabilities.FIREFOX
capabilities["marionette"] = True
firefox_bin = "/usr/bin/firefox"
browser = execute_with_retry(lambda: webdriver.Firefox(
    firefox_binary=firefox_bin, capabilities=capabilities), 10)

browser.get("https://www.google.com")

time.sleep(10)

browser.close()