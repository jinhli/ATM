#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/13/18

import os
import sys
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #整个程序的主目录

DATABASE = {
    'engine': 'file_storage', #support mysql,postgresql in the future
    'name': 'accounts',
    'path': "%s/db" % BASE_DIR
}


LOG_LEVEL = logging.INFO  #日志的级别
LOG_TYPES = {
             'transaction': 'transactions.log',
             'access': 'access.log',
}

TRANSACTION_TYPE = {
    'repay': {'action': 'plus', 'interest': 0},
    'withdraw': {'action': 'minus', 'interest': 0.005},
    'transfer': {'action': 'minus', 'interest': 0.005},
    'consume': {'action': 'minus', 'interest': 0},

}

