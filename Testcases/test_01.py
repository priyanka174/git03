from selenium.webdriver import Chrome
from Base import Base_01
from Libraries import data
from pages import pages1

def test_data01():
    driver=Base_01.startbrowser()
    reg=pages1.pages2(driver)
    reg.username("priy111")
    driver=Base_01.closebrwser()

def test_data02():
    driver=Base_01.startbrowser()
    reg=pages1.pages2(driver)
    reg.email("priyaaaaa")
    driver=Base_01.closebrwser()