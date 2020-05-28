#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File  : logger.py
# Author: wangqingbin8
# Time  : 2020-05-25 17:12:59
import os

from loguru import logger


class Loggings:
    __instance = None
    logger.add(f"logs/logger.log",
               rotation="500MB",
               encoding="utf-8",
               retention="30 days",
               compression="zip",
               enqueue=True
               )
    # 类单例模式运行logger
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Loggings, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def trace(self, msg):
        return logger.trace(msg)

    def debug(self, msg):
        return logger.debug(msg)

    def info(self, msg):
        return logger.info(msg)

    def success(self, msg):
        return logger.success(msg)

    def warning(self, msg):
        return logger.warning(msg)

    def error(self, msg):
        return logger.error(msg)

    def critical(self, msg):
        return logger.critical(msg)


if __name__ == '__main__':
    # print(os.path.dirname(os.getcwd()))
    logger.trace('logger.trace')
    logger.debug('logger.debug')
    logger.info('logger.info')
    logger.success('logger.success中文')
    logger.warning('logger.warning')
    logger.error('logger.error')
    logger.critical('logger.critical')
