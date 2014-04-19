# coding: utf-8
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import unittest
from MainPage import MainPage


class SimpleTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)

    def test_search_in_python_org(self):

        driver = self.driver
        driver.get("http://go.mail.ru")
        main_page = MainPage(driver)
        print(main_page.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()