# coding: utf-8

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(object):
    def __init__(self, driver):
        self.__driver = driver

    @property
    def title(self):
        return self.__driver.title

    @property
    def search_form(self):
        return SearchForm(self.__driver)

    @property
    def suggests(self):
        return Suggest(self.__driver)

    def clear_search_form(self):
        self.search_form.clear_text()

class SearchForm(object):
        def __init__(self, driver):
            self.__driver = driver

        def go(self):
            self.__driver.find_element_by_id('q').submit

        def enter_text(self, text):
            self.__driver.find_element_by_id('q').send_keys(text)
            return self

        @property
        def title(self):
            return self.__driver.title

        def get_text_form(self):
            return self.__driver.find_element_by_id('q').text

        def clear_text(self):
            self.__driver.find_element_by_id('q').clear()

class Suggest(object):
    def __init__(self, driver):
        self.__driver = driver

    def first_result(self):
        try:
            element = WebDriverWait(self.__driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "go-suggests__item__text"))
            )
            return element
        finally:
            pass