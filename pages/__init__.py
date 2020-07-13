#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by wangqingbin8 at 2020-06-28 11:46
import os

import yaml
from loguru import logger

ELEMENTS_PATH = os.getcwd() + '/pages/elements.yml'


class Yaml(object):

    def __init__(self):
        super(Yaml, self).__init__()
        self._data = None

    @property
    def data(self, path=ELEMENTS_PATH):
        """
        :param path: yaml文件路径
        :return:
        """
        if os.path.exists(path) and os.path.isfile(path):
            with open(path, mode='r', encoding='utf-8') as f:
                try:
                    self._data = yaml.safe_load(f)
                except Exception as e:
                    logger.error('YAML文件语法格式错误: {}'.format(e))
                else:
                    return self._data
        else:
            logger.error('找不到文件：{0}'.format(path))


if __name__ == '__main__':
    obj = Yaml()
    data = obj.data
    print(type(data))
    print(data)
