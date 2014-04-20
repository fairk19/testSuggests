# coding: utf-8
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from MainPage import MainPage
import unittest

class SimpleTests(unittest.TestCase):

    capabilities = None

    def setUp(self):
        self.driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)

        self.queries = ["dr", "вк"]
        self.driver.get("http://go.mail.ru")

    def test_popular_query(self):
        driver = self.driver
        main_page = MainPage(driver)
        for query in self.queries:
            main_page.search_form.enter_text(query)
            self.assertIn("вконтакте", main_page.suggests.first_result().text)
            main_page.clear_search_form()

    def test_content_search_form_after_submit(self):
        driver = self.driver
        main_page = MainPage(driver)
        main_page.search_form.enter_text("mail").go()
        main_page.search_form.clear_text()
        main_page.search_form.enter_text("mail")
        self.assertIn("mail.ru", main_page.suggests.first_result().text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()