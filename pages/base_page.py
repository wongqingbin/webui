#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File  : basepage.py
# Author: wangqingbin8
# Time  : 2020-05-25 16:00:57
# desc: https://www.selenium.dev/documentation/zh-cn/getting_started/
# desc: https://python-selenium-zh.readthedocs.io/zh_CN/latest/
import os
import time

from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.wait import WebDriverWait

from utils.read_yaml import get_yaml_element


class BasePage:

    def __init__(self, driver: webdriver):
        self.data = get_yaml_element('data/elements.yaml')
        self.driver = driver

    def find_element(self, locator: dict):
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

    def find_elements(self, locator: dict):
        pass

    def get_value(self, element):
        return element.get_attribute('value')

    def get_alert(self):
        # alerts、confirms、prompts等对话框
        # TODO alter对象 可以做确定、忽略、阅读提示文本或者甚至输入prompt
        # alert = self.driver.switch_to_alert()

        # 自动确认alter弹窗
        # Wait for the alert to be displayed and store it in a variable
        alert = wait.until(expected_conditions.alert_is_present())
        # Store the alert text in a variable
        text = alert.text
        # Press the OK button
        alert.accept()

        # 自动确认Confirm确认框
        # Wait for the alert to be displayed
        wait.until(expected_conditions.alert_is_present())
        # Store the alert in a variable for reuse
        alert = driver.switch_to.alert
        # Store the alert text in a variable
        text = alert.text
        # Press the Cancel button
        alert.dismiss()

        # 自动处理Prompt提示框
        # Wait for the alert to be displayed
        wait.until(expected_conditions.alert_is_present())
        # Store the alert in a variable for reuse
        alert = Alert(driver)
        # Type your message
        alert.send_keys("Selenium")
        # Press the OK button
        alert.accept()

    def events(self):
        """ 示例 """
        # 浏览器向前
        self.driver.forward()
        # 浏览器向后
        self.driver.back()
        # And now output all the available cookies for the current URL
        self.driver.get_cookies()
        # 获取当前url
        self.driver.current_url
        # 获取当前url的网页标题
        self.driver.title
        # 刷新页面
        self.driver.refresh()
        # 获取当前窗口(返回窗口ID)
        self.driver.current_window_handle
        # 切换窗口或标签页  PS:该特性适用于 Selenium 4 及其后续版本
        # self.driver.switch_to.new_window('window')  # 'tab'
        # 获取窗口大小
        # 或者存储尺寸并在以后查询它们
        size = self.driver.get_window_size()
        width = size.get("width")
        height = size.get("height")
        # 最大化窗口
        self.driver.maximize_window()

    def _waits(self):
        # # 显示wait 使用expected_condition类处理各种情况
        # wait = WebDriverWait(driver, 10)
        # element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))

        # # 隐式等待
        # self.driver.implicitly_wait(10) # seconds

        # 程序死等 time.sleep()
        pass

    def save_png(self):
        picture_time = time.strftime(
            "%Y-%m-%d--%H_%M_%S", time.localtime(time.time()))
        directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        try:
            File_Path = os.getcwd() + '\\images\\' + directory_time + '\\'
            if not os.path.exists(File_Path):
                os.makedirs(File_Path)
        except Exception as e:
            logger.error("创建截图目录失败: {}".format(e))
        try:
            flag = self.driver.save_screenshot(
                '.\\images\\' + directory_time + '\\' + picture_time + '.png')
            if flag:
                logger.info('截图保存成功{}'.format(flag))
        except Exception as e:
            logger.error("截图失败: {}".format(e))
        try:
            # 返回allure存储截图格式
            return self.driver.get_screenshot_as_png()
        except Exception as e:
            logger.error('allure截图保存失败: {}'.format(e))
            return
