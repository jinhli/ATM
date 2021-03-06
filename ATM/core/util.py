#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__="Bonnie"
# Date:2018/3/16
import hashlib
from core import db_handler
from core import transaction
from conf import settings


def print_log(msg, log_type='info'):
    """写个通用的打印log 的程序"""
    if log_type == 'info':
        print('\033[32;1m%s\033[0m' % msg)
    elif log_type == 'error':
        print('\033[31;1m%s\033[0m' % msg)


def passwd_md5(account, password):
    """

    :param account:
    :param password:
    :return:  MD5 密码
    """

    md5 = hashlib.md5(account.encode('utf-8'))  #带上用户名加密
    md5.update(password.encode('utf-8'))   #加上encode编码
    ret = md5.hexdigest()
    return ret


# def com_input(msg):
#     input('\033[32;1m%s\033[0m' % msg)

# a = passwd_md5('luffy','1234')
# print(a)