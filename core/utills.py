#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/14/18

def print_log(msg, log_type='info'):
    """写个通用的打印log 的程序"""
    if log_type == 'info':
        print('\033[32;1m%s\033[0m'%msg)
    elif log_type == 'error':
        print('\033[31;1m%s\033[0m'%msg)

