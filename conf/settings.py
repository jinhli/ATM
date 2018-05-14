#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/13/18

import os
import sys
import logging

BASE_DIR = os.path.basename(os.path.basename(os.path.abspath(__file__))) #整个程序的主目录

# DATABASE = {
#     'engine': 'file_storage', #support mysql,postgresql in the future
#     'name':'accounts',
#     'path': "%s/db" % BASE_DIR
# }


LOG_LEVEL = logging.INFO #日志的级别
LOG_TYPES = {"""日志类型，分为操作日志和登陆日志"""
    'transaction': 'transactions.log',
    'access': 'access.log',
}

TRANSACTION_TYPE = {"""操作类型，还款，取现，转帐，"""
    'repay':{'action':'plus', 'interest':0},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'minus', 'interest':0.05},
    'consume':{'action':'minus', 'interest':0},

}

