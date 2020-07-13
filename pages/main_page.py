#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by wangqingbin8 at 2020-05-25 16:01:36
import time
from typing import Text

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from pages import Yaml
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.search_page import SearchPage


class MainPage(BasePage):
    el: WebElement

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._yaml = Yaml()

    def open_url(self):
        url = self._yaml.data['conf']['url']
        self._driver.get(url)
        self._driver.maximize_window()
        time.sleep(1)
        return self._driver.current_url

    def more(self):
        locator = self._yaml.data['main']['more']
        self.el = self.find_element(locator)
        self.el.click()
        return HomePage(self._driver)

    def search(self, keyword: Text):
        locator = self._yaml.data['main']['search']
        self.el = self.find_element(locator)
        self.el.clear()
        self.el.send_keys(keyword)
        self.el.send_keys(Keys.ENTER)
        return SearchPage(self._driver)

    def categories(self):
        locator = self._yaml.data['main']['categories']
        self.el = self.find_element(locator)
        self.el.click()

    def tags(self):
        locator = self._yaml.data['main']['tags']
        self.el = self.find_element(locator)
        self.el.click()
