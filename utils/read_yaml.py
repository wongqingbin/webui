#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# File  : read_yaml.py
# Author: wangqingbin8
# Time  : 2020-05-25 15:44:31
import os
import yaml

# from logger import Loggings
from loguru import logger

# logger = Loggings()

def get_yaml_data(path):
    """读取yaml数据
    :param path路径
    :return dict
    example: 
        data = get_data('example/resource.yaml')
        if isinstance(data, dict):  # isinstance(data, list):
            for d in data:
                print(d)
    """
    if os.path.exists(path) and os.path.isfile(path):
        with open(path, mode='r', encoding='utf-8') as f:
            try:
                data = yaml.full_load(f)  # full_load加载全部数据
                return data
            except Exception as e:
                logger.error('YAML文件语法格式错误: {}'.format(e))
                return None
    else:
        logger.error('找不到文件：{0}'.format(path))
        return None

def get_yaml_element(path):
    datas = get_yaml_data(path)
    if not datas:
        return None
    names = []
    locators = []
    for data in datas:
        try:
            names.append(data.pop('name'))
            tmp = (data.pop('selector'), data.pop('value'))
        except Exception as e:
            logger.error(e)
            return None
        locators.append(tmp)
    results = dict(zip(names, locators))
    return results


if __name__ == "__main__":
    data = get_yaml_element('data/elements.yaml')
    logger.info(data)
    logger.info(1111111111)
    locator = data['search']
    logger.info(locator)
    logger.info(111111111111)
    logger.info(locator[0], locator[1])
    # print(data[0])
    # print(type(data))  # list
    # data = dict(data)
    # if isinstance(data, list):
    #     for d in data:
    #         print(d)
