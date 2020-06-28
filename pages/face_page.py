#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by wangqingbin8 at 2020-06-28 11:46
"""Description"""
from pages.base_page import BasePage
from utils.read_yaml import get_yaml_element


class FacePage(BasePage):
    def __init__(self, driver):
        super(FacePage, self).__init__(driver)
        self.data = get_yaml_element('data/face.yml')

    def slide_el(self):
        """滑动到和元素相同位置"""
        locator = self.data.get('send_image_url')
        element = self.find_element(locator)
        self._driver.execute_script("arguments[0].scrollIntoView();", element)

    def send_img_url(self):
        locator = self.data.get('send_image_url')
        element = self.find_element(locator)
        element.send_keys('http://wang.com/dfdsf/sdfdsf.jpg')

    def click_url(self):
        locator = self.data.get('detect_img_url')
        element = self.find_element(locator)
        element.click()

    def local_file(self, path):
        locator = self.data.get('upload_file')
        self.upload_file(locator, path)

