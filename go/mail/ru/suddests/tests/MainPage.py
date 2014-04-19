# coding: utf-8


class MainPage(object):
    def __init__(self, driver):
        self.__driver = driver

    @property
    def title(self):
        return self.__driver.title

    @property
    def search_form(self):
        return SearchForm(self.__driver)

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
