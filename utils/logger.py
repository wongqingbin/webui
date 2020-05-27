#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File  : logger.py
# Author: wangqingbin8
# Time  : 2020-05-25 17:12:59
import logging
import logging.config
import os


class Logger(object):

    def __init__(self) -> None:
        self.con_log = 'utils/logger.conf'
        logging.config.fileConfig(self.con_log)
        self.logger = logging.getLogger()
        super().__init__()


if __name__ == '__main__':
    print(os.path.dirname(os.getcwd()))
