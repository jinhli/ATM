#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/14/18

import json
import os
import time
from conf import settings
from core import util
import sys
#
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #整个程序的主目录
# sys.path.append(BASE_DIR)


def load_file(account):
    """
    :param account:
    :return: user_info
    :用户信息读到内存
    """
    # user_info = {} #可以不需要提前定义
    file_name = '%s/account/%s.json' % (settings.BASE_DIR, account)
    if os.path.isfile(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            user_info = json.load(f)
            return user_info
    else:
        util.print_log('there is no account info for %s' % account, 'error')
        exit()


def update_file(account, user_info):
    """
    更新这里， 保证所有的修改都能使用
    :param account:
    :return: no return
    用户信息更新到文件
    """
    file_name = '%s/account/%s.json' % (settings.BASE_DIR, account)

    with open('%s.new' %file_name, 'w', encoding='utf-8') as f:
        json.dump(user_info, f)

    os.rename('%s.new' %file_name,file_name) #目的是以防万一出现老数据被修改，新数据又没又完成

    return True


