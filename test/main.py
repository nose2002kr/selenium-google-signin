from selenium_google_login import launch_selenium
from selenium_google_login import login_to_google

if __name__ == '__main__':
    driver = launch_selenium('/path/whare/chromedriver')
    login_to_google(driver)
    driver.quit()
