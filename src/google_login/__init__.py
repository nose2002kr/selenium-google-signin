from ._google_login import login_to_google 

from selenium import webdriver
def launch_selenium(driver_path: str = None) -> webdriver.Chrome:
    from ._util import SeleniumUtil
    return SeleniumUtil.launch_selenuim(driver_path)
