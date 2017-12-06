import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Event_MCP(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_event(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://midcityproject.pythonanywhere.com/")
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/nav/div/ul[2]/li/a[2]").click()  #sign in
        elem = driver.find_element_by_name("username")
        elem.send_keys(user)
        elem = driver.find_element_by_name("password")
        elem.send_keys(pwd)
        time.sleep(5)
        elem.send_keys(Keys.RETURN)

        #elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/input[2]").click() #login
        driver.get("http://midcityproject.pythonanywhere.com/")
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div[6]/a").click() #view all events
        driver.get("http://midcityproject.pythonanywhere.com/events/")
        time.sleep(8)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[5]/div/div[2]/a[3]").click() #event signup
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/form/button").click()#save button
        time.sleep(3)
        def tearDown(self):
            self.driver.close()
