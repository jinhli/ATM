#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/14/18
import os
from core import db_handler
from conf import settings
from core import logger
from core import util
import json
import time
from core import main

def login_required(func):
    """
    验证用户登陆
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        # print('--wrapper--->',args,kwargs)

        if args[0].get('is_authenticated'):
            return func(*args, **kwargs)
        else:
            exit('user is not authenticated')
    return wrapper


def access_auth(account, password):
    """

    :param account:
    :param password:
    :return: account_data
    """
    db_path = '%s/account' % settings.BASE_DIR

    print(db_path)

    account_file = '%s/%s.json' % (db_path, account)
    if os.path.isfile(account_file):
        account_data = db_handler.load_file(account)
        if account_data['status'] == 1:  # the account is locked
            util.print_log('your account has been locked, please contact the administrator', 'error')
            option = input('please press b to quit')
            if option == 'b':
                exit('quit the system')
        if account_data['status'] == 0:
            password_md5 = util.passwd_md5(account, password)
            if password_md5 == account_data['password']:
                expire_time = time.mktime(time.strptime(account_data['expire_date'],'%Y-%m-%d'))
                if time.time() > expire_time:
                    util.print_log('the account %s has been expired, please contact the bank' % account, 'error')
                    exit()
                else:
                    util.print_log('welcome %s \o/'%account,'info')
                    main.access_logger.info('%s access the ATM successfully' % account)

                return account_data
            else:
                util.print_log('the password of the account %s is not right' % account, 'error')
        else:
            util.print_log('there is no any information of %s' % account, 'error')
            exit()


def user_login(user_data, log_obj):
    """
    登陆函数
    :param user_data:
    :param log_obj:
    :return:
    """
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3:
        account = input('please input your account->').strip()
        password = input('please input your password->').strip()
        account_data = access_auth(account, password)
        if account_data:
            user_data['is_authenticated'] = True  # login successfully
            user_data['account_name'] = account
            return account_data
        retry_count += 1
    else:
        user_info = db_handler.load_file(account)
        user_info['status'] = 1
        db_handler.update_file(account,user_info)
        log_obj.error("[%s]账户太多次尝试" % account)  # log type
        exit()



