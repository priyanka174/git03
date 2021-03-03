from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Libraries import data

def startbrowser():
    global driver
    if((data.data1('info', 'Browser'))=='Chrome'):
        path="C:/Users/User/PycharmProjects/github03/Drivers/chromedriver.exe"
        driver=Chrome(executable_path=path)
    else:
        path="C:/Users/User/PycharmProjects/github03/Drivers/geckodriver-v0.26.0-win64 (1)/geckodriver.exe"
        driver=Firefox(executable_path=path)
    driver.maximize_window()
    driver.get(data.data1('info', 'Application_URL'))
    return driver
def closebrwser():
     driver.close()

