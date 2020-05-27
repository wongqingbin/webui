#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File  : conftest.py
# Author: wangqingbin8
# Time  : 2020-05-25 16:03:54
import os

import pytest
from selenium import webdriver

from pages.main_page import MainPage
from utils.logger import Logger


@pytest.fixture()
def make_driver():
    driver: webdriver = None
    CHROMEDRIVER_PATH = os.getcwd() + r'\libs\chromedriver.exe'
    Logger().logger.info('CHROMEDRIVER路径: {0}'.format(CHROMEDRIVER_PATH))

    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
    driver.implicitly_wait(30)
    if driver:
        Logger().logger.info('dirver创建成功success')
        Logger().logger.info('全局隐式等待implicitly_wait: 30s')
    else:
        Logger().logger.info('dirver创建失败fail')
    obj = MainPage(driver)
    yield obj
    driver.quit()
