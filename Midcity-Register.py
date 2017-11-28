import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Reg_MCP(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_mcp(self):
        user = "AbeerM"
        fname = "Abeer"
        mail = "barun120@uno.com"
        pwd1 = "arun100"
        pwd2 = "arun100"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://midcityproject.pythonanywhere.com/")
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/nav/div/ul[2]/li/a[1]").click()
        driver.get("http://midcityproject.pythonanywhere.com/register/")
        time.sleep(5)
        elem = driver.find_element_by_name("username")
        elem.send_keys(user)
        elem = driver.find_element_by_name("first_name")
        elem.send_keys(fname)
        elem = driver.find_element_by_name("email")
        elem.send_keys(mail)
        elem = driver.find_element_by_name("password")
        elem.send_keys(pwd1)
        elem = driver.find_element_by_name("password2")
        elem.send_keys(pwd2)
        time.sleep(6)
        elem.send_keys(Keys.RETURN)

        #elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/input").click()
        #time.sleep(2)
        #driver.get("http://midcityproject.pythonanywhere.com/register/")
        assert "registered!"
        time.sleep(5)

        def tearDown(self):
            self.driver.close()

