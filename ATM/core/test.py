#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__="Bonnie"
# Date:2018/3/16
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #整个程序的主目录
sys.path.append(BASE_DIR)
print(BASE_DIR)
from conf import settings
from core import util
import re



def pay_check():

    count = 0
    exit_flag = False
    log_name = '%s/log/luffy.log' % settings.BASE_DIR
    # user_name = user_data['account_name']
    while not exit_flag:

        search_mon = input('please input the month of the log you want to search, "example = 2018-01",'
                           ' or input "b" to quit >>:').strip()
        if search_mon == 'b':
            return
        else:
            if os.path.isfile(log_name):
                with open(log_name, 'r') as f:
                    for line in f:
                        search_res = re.match(search_mon, line)
                        if search_res:
                            util.print_log(line, 'info')
                            count += 1
                    util.print_log('Above are the consume log, total %s' % count, 'info')
            else:
                util.print_log('there is no consume log', 'error')
                exit_flag = True

pay_check()