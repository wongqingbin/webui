#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File  : conftest.py
# Author: wangqingbin8
# Time  : 2020-05-25 16:03:54
import os

import pytest
from loguru import logger
from selenium import webdriver

from pages.main_page import MainPage

CHROMEDRIVER_PATH = os.getcwd() + r'\libs\chromedriver.exe'


# "function" (default), "class", "module", "package" or "session"
# function/函数级（测试用例）、class/类级（测试类）、module/模块级（测试模块—py文件）、session/会话级（整个测试执行会话）
@pytest.fixture(scope='class')
def make_driver():
    driver: webdriver = None
    logger.info('CHROMEDRIVER路径: {0}'.format(CHROMEDRIVER_PATH))

    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
    driver.implicitly_wait(30)
    if driver:
        logger.info('driver创建成功success')
        logger.info('全局隐式等待implicitly_wait: 30s')
    else:
        logger.info('driver创建失败failed')
    obj = MainPage(driver)
    yield obj  # 1.返回值; 2.setup、teardown分隔
    driver.quit()
