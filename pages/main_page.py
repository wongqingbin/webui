#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File  : mainpage.py
# Author: wangqingbin8
# Time  : 2020-05-25 16:01:36
from pages.base_page import BasePage
from pages.face_page import FacePage
from utils.read_yaml import get_yaml_element


class MainPage(BasePage):

    def __init__(self, driver):
        self._driver = driver
        self.data = get_yaml_element('data/main.yml')
        super().__init__(driver)

    def open_url(self, url):
        self._driver.get(url)
        # 通过代理的方式打开url
        #PROXY = "<HOST:PORT>"
        # webdriver.DesiredCapabilities.CHROME['proxy'] = {
        #    "httpProxy": PROXY,
        #    "ftpProxy": PROXY,
        #    "sslProxy": PROXY,
        #    "proxyType": "MANUAL",
        #}
        #self.driver.get(url)
        return self._driver.current_url

    def enter_face(self):
        locator = self.data.get('enter_face')
        element = self.find_element(locator)
        element.click()
        self.switch_tag()  # 切换新开页
        return FacePage(self._driver)
