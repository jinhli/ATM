#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/14/18
import time
import os
import sys
import re
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  #整个程序的主目录
sys.path.append(BASE_DIR)

from core import auth
from core import logger
from core import db_handler
from core import transaction
from core.auth import login_required
from core import util
from conf import settings
from core import manage
from shopping_mall import shopping_mall


# logger
trans_logger = logger.logger('transaction')
access_logger = logger.logger('access')


# 临时账户数据
user_data = {
    'account_name': None,
    'is_authenticated': False,
    'account_data': None

}


def account_info(user_data):
    """
    打印用户信息
    :param user_info:
    :return:
    """
    # user_info = db_handler.load_file(user_data['account_name'])
    user_info = user_data['account_data']
    print('ACCOUNT INFO'.center(50, '-'))
    for k, v in user_info.items():  # ???
        if k not in ('password',):
            util.print_log('%15s: %s' % (k, v), 'info')
    print('END'.center(50, '-'))


def com_tran_module(user_data, tran_type):
    """
    交易交互模块
    :param user_data:
    :return: user_info , and back_flag
    """
    user_info = db_handler.load_file(user_data['account_name'])#user_data 全局变量
    balance_info = ''' --------- bank info --------
            credit: %s
            balance: %s''' % (user_info['credit'], user_info['balance'])

    util.print_log(balance_info, 'info')
    back_flag = False
    while not back_flag:
        if tran_type in settings.TRANSACTION_TYPE:
            amount = input('please input the transaction amount>>:').strip()
            if len(amount)>0 and amount.isdigit():
                amount = float(amount)
                if tran_type == 'transfer':
                    transfer_name1 = input('please input the account you want to transfer>>:').strip()
                    if transfer_name1 == 'b' or amount == 'b':
                        return
                    file_name = '%s/account/%s.json' % (settings.BASE_DIR, transfer_name1)
                    if os.path.isfile(file_name):
                        new_balance, save_flag = transaction.make_transaction(trans_logger, user_info, tran_type, amount, transfer_name = transfer_name1)

                else:
                    new_balance, save_flag = transaction.make_transaction(trans_logger, user_info, tran_type, amount)
                if save_flag:
                    util.print_log('transaction successfully', 'info')
                    util.print_log('current balance>>%s' % new_balance['balance'], 'info')
                else:
                    util.print_log('there is some thing wrong and the transaction is not success', 'error')

            elif amount == 'b':
                back_flag = True


@login_required  # 装饰器，判断用户是否登陆
def repay(user_data):
    """
    还款
    :param user_info:
    :return:
    """
    com_tran_module(user_data, 'repay')




@login_required
def transfer(user_data):
    """
    转账
    :param user_data:
    :return:
    """
    com_tran_module(user_data, 'transfer')


@login_required
def withdraw(user_data):
    """
    with_draw
    :param user_data:
    :return:
    """
    com_tran_module(user_data, 'withdraw')


@login_required
def consume(user_data):
    """
    pay_check
    :param user_data:
    :return:
    """
    name = user_data['account_name']
    shopping_mall.shopping(name, logger.logger_consume(name))
    com_tran_module(user_data, 'consume')


@login_required
def pay_check(user_data):
    """
    pay_check
    :param user_data:
    :return:
    """
    count = 0
    exit_flag = False
    user_name = user_data['account_name']
    log_name = '%s/log/%s.log' % (settings.BASE_DIR, user_name)
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


def logout(user_data):
    """
    logout
    :param user_data:
    :return:
    """
    exit('quit the system')


def user_interface(account_data):
    """
    #用户交互函数
    interact with user:
    :return:
    """
    menu = u"""
    -------Bank interface ---------
    1.account_info
    2.  repay 
    3.  withdraw 
    4.  transfer 
    5.  consume
    6.  pay_check
    7.  logout
    """
    menu1 = u"""
    -------Bank interface ---------
    1.  account_info
    2.  repay 
    3.  withdraw 
    4.  transfer 
    5.  consume 
    6.  pay_check
    7.  logout
    8.  Administrator
    """
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': consume,
        '6': pay_check,
        '7': logout,
    }  # 函数字典， 实际上每个选项对应一个函数
    admin_flag = account_data['admin_flag']
    exit_flag = False
    while not exit_flag:
        if admin_flag == 1:  # 管理员
            util.print_log(menu1, 'info')
            menu_dic['8'] = manage.manage_main
        else:
            util.print_log(menu,'info')
        user_option = input('>>:').strip()
        if user_option == 'b':
            return
        if user_option in menu_dic:
            menu_dic[user_option](user_data)
        else:
            util.print_log('your choice does not exist', 'error')


def run():
    user_info = auth.user_login(user_data, access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = user_info
        user_interface(user_data['account_data'])
