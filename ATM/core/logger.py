#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/13/18


import logging
import os
import sys
from conf import settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #整个程序的主目录
sys.path.append(BASE_DIR)


def logger(log_type):
    #create logger
    logger = logging.getLogger(log_type)
    # logger = logging.getLogger('access.log')
    logger.setLevel(settings.LOG_LEVEL)
    # logger.setLevel(logging.INFO)

    #create console handle
    # ch = logging.StreamHandler()
    # ch.setLevel(settings.LOG_LEVEL)
    # ch.setLevel(logging.INFO)

    #create file handle
    log_file = '%s/log/%s' %(settings.BASE_DIR, settings.LOG_TYPES[log_type])
    # log_file = '%s' % ('access.log')
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)
    # fh.setLevel(logging.INFO)

    #create the formatter
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

    # ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    #add ch and fh to logger
    # logger.addHandler(ch)
    logger.addHandler(fh)

    # logger.info('bonnie has access')

    return logger


# logger('transaction')

