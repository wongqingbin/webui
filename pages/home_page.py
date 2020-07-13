#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by wangqingbin8 at 2020-07-13 18:27
"""Description"""
from typing import Text

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from pages import Yaml
from pages.base_page import BasePage


class HomePage(BasePage):
    el: WebElement

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self._yaml = Yaml()

    def categories(self):
        locator = self._yaml.data['home']['categories']
        self.el = self.find_element(locator)
        self.el.click()

    def article(self):
        locator = self._yaml.data['home']['article']
        self.el = self.find_element(locator)
        self.el.click()

    def tags(self):
        locator = self._yaml.data['home']['tags']
        self.el = self.find_element(locator)
        self.el.click()

    def archives(self):
        locator = self._yaml.data['home']['archives']
        self.el = self.find_element(locator)
        self.el.click()

    def more(self):
        locator = self._yaml.data['home']['more']
        self.el = self.find_element(locator)
        self.el.click()

    def home(self):
        locator = self._yaml.data['home']['home']
        self.el = self.find_element(locator)
        self.el.click()

    def frieza(self):
        locator = self._yaml.data['home']['frieza']
        self.el = self.find_element(locator)
        self.el.click()
