#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File  : mainpage.py
# Author: wangqingbin8
# Time  : 2020-05-25 16:01:36
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_url(self, url):
        self.driver.get(url)
        return self.driver.current_url

    def search(self, keyword):
        locator = self.data.get('search')
        element = self.find_el(locator)
        element.send_keys(keyword)
        text = self.get_value(element)
        return text
