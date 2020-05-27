#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File  : test_case.py
# Author: wangqingbin8
# Time  : 2020-05-25 14:03:54
import time

import pytest
from loguru import logger
from selenium import webdriver


class TestCase():

    @pytest.mark.usefixtures('make_driver')
    @pytest.mark.parametrize('url', [('https://wongqingbin.github.io')])
    def test_demo1(self, make_driver, url):
        obj = make_driver  # 从conftest.py中获取对象
        try:
            logger.info('info开始打开url')
            obj.open_url(url)
            text = obj.search('hello world')
            logger.info(text)
            assert text == 'hello world'
            logger.info('end...')
            time.sleep(3)
        except Exception as e:
            logger.error(e)

    # @pytest.mark.parametrize('url', [('https://wongqingbin.github.io')])
    # def test_demo2(self, url):
    #     dirver = webdriver.Chrome(
    #         executable_path=r'C:\Users\wangqingbin8\VScodeProjects\uiautomation\libs\chromedriver.exe')
    #     dirver.get(url)
    #     element = dirver.find_element(By.CSS_SELECTOR, 'body > div.cover-wrapper > cover > div.cover-body > div.b > div.m_search > form > input')
    #     print(element.get_attribute('value'))
    #     el = element.send_keys('hello world')
    #     print(element.get_attribute('value'))
    #     time.sleep(5)


if __name__ == "__main__":
    pytest.main('-s', '-q')
