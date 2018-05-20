#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/13/18


import logging
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #整个程序的主目录
sys.path.append(BASE_DIR)

from conf import settings



def logger(log_type):
    #create logger
    logger = logging.getLogger(log_type)
    # logger = logging.getLogger('access.log')
    logger.setLevel(settings.LOG_LEVEL)

    #create file handle
    log_file = '%s/log/%s' %(settings.BASE_DIR, settings.LOG_TYPES[log_type])

    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)

    #create the formatter
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

    fh.setFormatter(formatter)

    #add ch and fh to logger

    logger.addHandler(fh)

    return logger


def logger_consume(name):
    # create logger
    logger_consume = logging.getLogger(name)
    # logger = logging.getLogger('access.log')
    logger_consume.setLevel(settings.LOG_LEVEL)

    # create file handle
    log_file = '%s/log/%s.log' % (settings.BASE_DIR, name)

    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)

    # create the formatter
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

    fh.setFormatter(formatter)

    # add ch and fh to logger

    logger_consume.addHandler(fh)

    return logger_consume

# logger_consume('huahua')

