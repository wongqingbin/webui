#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File  : test_case.py
# Author: wangqingbin8
# Time  : 2020-05-25 14:03:54
import os
import time

import allure
import pytest
from loguru import logger


@allure.feature('这里TestCase feature')
class TestCase(object):

    @allure.story('1这里是story')
    @allure.title('打开url首页')
    @allure.issue("http://www.jira.com")
    @allure.testcase("http://www.testlink.com")
    @pytest.mark.usefixtures('make_driver')
    # @pytest.mark.parametrize('url', [('http://jddbrain.jdfmgt.com')])
    def test_search(self, make_driver):
        """
        用例描述：这是用例描述，Test case 01，描述本人
        """
        obj_main = make_driver  # 从conftest.py中获取对象
        # try:
        logger.info('打开网页')
        obj_main.open_url()
        obj_main.save_png()
        logger.info('搜索内容')
        obj_search = obj_main.search('python')
        time.sleep(3)
        obj_search.save_png()
        logger.info('关闭搜索框')
        obj_search.close()
        time.sleep(1)
        # assert text == 'hello world'
        # # with allure.step('添加失败截图...'):
        # allure.attach(obj_face.save_png(), "输入hello world失败", allure.attachment_type.PNG)
        logger.info('end...')
        # except Exception as e:
        #     logger.error(e)
        #     allure.attach(obj_face.save_png(), "输入hello world失败", allure.attachment_type.PNG)

    @allure.story('2这里是story')
    def test_home(self, make_driver):
        """
        用例描述：这是用例描述，Test2
        """
        obj_main = make_driver
        obj_home = obj_main.more()
        logger.info('分类列表')
        obj_home.categories()
        obj_home.save_png()
        logger.info('标签列表')
        obj_home.tags()
        obj_home.save_png()
        logger.info('系列文章')
        obj_home.archives()
        obj_home.save_png()

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
    pytest.main(args=['-s', '-q', '--alluredir=allure/results'])
    os.popen('allure generate allure/results -o allure/report --clean')
    os.popen('allure serve allure/results')
