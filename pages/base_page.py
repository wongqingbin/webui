#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File  : basepage.py
# Author: wangqingbin8
# Time  : 2020-05-25 16:00:57
from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.read_yaml import get_yaml_element


class BasePage:

    def __init__(self, driver: webdriver):
        self.data = get_yaml_element('data/elements.yaml')
        self.driver = driver

    def find_el(self, locator: dict):
        """
        By对象定位方式:
            ID = "id"
            XPATH = "xpath"
            LINK_TEXT = "link text"
            PARTIAL_LINK_TEXT = "partial link text"
            NAME = "name"
            TAG_NAME = "tag name"
            CLASS_NAME = "class name"
            CSS_SELECTOR = "css selector"
        示例:
            find_el({'CSS_SELECTOR', 'body > div.cover-wrapper >'})
        参数解读:
            locator 为字典类型
                key == By对象的定位方式, 类型string, 使用getattr()字符串反射调用By对象
                value == 元素控件定位值, 类型string
        """
        try:
            element = self.driver.find_element(by=getattr(
                By, locator[0]), value=locator[1])
            return element
        except Exception as e:
            logger.error(e)

    def get_value(self, element):
        return element.get_attribute('value')
