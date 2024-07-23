from google_login import login_to_google
from google_login import launch_selenium

if __name__ == '__main__':
    driver = launch_selenium('chromedriver.exe')
    login_to_google(driver=driver)
    driver.quit()
