#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by wangqingbin8 at 2020-06-28 11:46
"""Description"""
from selenium.webdriver.remote.webelement import WebElement

from pages import Yaml
from pages.base_page import BasePage


class SearchPage(BasePage):
    el: WebElement

    def __init__(self, driver):
        super(SearchPage, self).__init__(driver)
        self._yaml = Yaml()

    def close(self):
        locator = self._yaml.data['search']['close']
        self.el = self.find_element(locator)
        self.el.click()

    def slide_el(self):
        """滑动到和元素相同位置"""
        locator = self._yaml.data.get('send_image_url')
        element = self.find_element(locator)
        self._driver.execute_script("arguments[0].scrollIntoView();", element)
