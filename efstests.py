import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Stock_EFS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_efs(self):
       user = "instructor"
       pwd = "instructor1a"
       cust = "12056"
       symbol = "NP"
       name = "NewPort"
       shares = "200"
       pprice = "30"

       driver = self.driver
       driver.maximize_window()
       driver.get("https://humna-efsblog.herokuapp.com/")
       time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.get("https://humna-efsblog.herokuapp.com/accounts/profile/")
       time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[3]/div/div/p[2]/a").click()
       driver.get("https://humna-efsblog.herokuapp.com/stock/")
       time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
       driver.get("https://humna-efsblog.herokuapp.com/stock/create/")
       time.sleep(5)

       elem = driver.find_element_by_name("customer")
       elem.send_keys(cust)
       elem = driver.find_element_by_name("symbol")
       elem.send_keys(symbol)
       elem = driver.find_element_by_name("name")
       elem.send_keys(name)
       elem = driver.find_element_by_name("shares")
       elem.send_keys(shares)
       elem = driver.find_element_by_name("purchase_price")
       elem.send_keys(pprice)

       time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
       time.sleep(5)
       assert "Stock added"

       def tearDown(self):
           self.driver.close()
