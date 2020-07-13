# #!/usr/bin/env python
# # -*- encoding: utf-8 -*-
# # File  : app_page.py
# # Author: wangqingbin8
# # Time  : 2020-05-25 16:03:31
# import os

# from selenium import webdriver

# from utils.logger import Logger as Log
# from pages.main_page import MainPage


# class App():
#     driver: webdriver = None
#     CHROMEDRIVER_PATH = os.getcwd() + r'\libs\chromedriver.exe'
#     Log().logger.info('CHROMEDRIVER路径: {0}'.format(CHROMEDRIVER_PATH))

#     @classmethod
#     def create_driver(cls):
#         cls.driver = webdriver.Chrome(executable_path=cls.CHROMEDRIVER_PATH)
#         cls.driver.implicitly_wait(30)
#         if cls.driver:
#             Log().logger.info('dirver创建成功success')
#             Log().logger.info('全局隐式等待implicitly_wait: 30s')
#         else:
#             Log().logger.info('dirver创建失败fail')
#         return MainPage(cls.driver)

#     @classmethod
#     def quit_driver(cls):
#         cls.driver.quit()
#         Log().logger.info('dirver退出成功')
