#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/14/18

from core import auth
from core import logger
from core import db_handler
from core import transaction
from core.auth import login_required
import time
from core import util

# logger
trans_logger = logger.logger('transaction')
access_logger = logger.logger('access')

# 临时账户数据
user_data = {
    'account_name': None,
    'is_authenticated': False,
    'account_data' : None

}


def account_info(user_info):
    """
    打印用户信息
    :param user_info:
    :return:
    """
    # user_info_list = user_info
    # info_dispay = u"""
    # ------- account_info ---------
    # name:%s
    # expire_date:%s
    # pay_day:%s
    # balance:%s
    # """%(user_info['id'],user_info['expire_date'],user_info['pay_day'],user_info['balance'])
    # print_log(info_dispay,'info')
    print('ACCOUNT INFO'.center(50, '-'))
    for k, v in user_info['data'].items():  # ???
        if k not in ('password',):
            print_log('%15s:%s' % (k, v))
        print('END'.center(50, '-'))


@login_required  # 装饰器，判断用户是否登陆
def repay(user_info):
    """
    还款
    :param user_info:
    :return:
    """
    pass


@login_required
def transfer(user_info):
    """
    转账
    :param user_info:
    :return:
    """
    current_balance = user_info['balance']

    balance_info = ''' --------- 银行信息 --------
            信用额度: %s
            账户余额: %s''' % (user_info['credit'], user_info['balance'])

    util.print_log(balance_info, 'info')
    back_flag = False
    while not back_flag:

        transfer_name = input('please input the account you want to transfer>>:').strip()
        transfer_amount = float(input('please input the amount>>:').strip())
        if transfer_name or transfer_amount == 'b':
            return
        if len(transfer_amount) > 0 and transfer_amount.isdigit():
            transfer_info = db_handler.load_file(transfer_name)
            user_info['balance'] = current_balance-transfer_amount
            transfer_info['balance'] = float(transfer_info['balance']+transfer_amount)
            db_handler.update_file(user_info['id'], user_info)
            db_handler.update_file(transfer_name, transfer_info)


@login_required
def with_draw(user_info):
    """
    with_draw
    :param user_info:
    :return:
    """
    pass


def logout(user_info):
    """
    logout
    :param user_info:
    :return:
    """
    exit('quit the system')


def user_interface(user_info):
    """
    #用户交互函数
    interact with user:
    :return:
    """
    menu = u"""
    ------- luff Bank ---------
    1.account_info
    2.  repay 
    3.  withdraw 
    4.  transfer 
    5.  pay_check
    6.  logout
    """
    menu_dic = {
        '1': 'account_info',
        '2': 'repay',
        '3': 'withdraw',
        '4': 'transfer',
        '5': 'pay_check',
        '6': 'logout',
    }  # 函数字典， 实际上每个选项对应一个函数
    exit_flag = False
    while not exit_flag:
        util.print_log(menu, 'info')
        user_option = input('>>:').strip()
        if user_option == 'b':
            return
        if user_option in menu_dic:
            menu_dic[user_option](user_info)
        else:
            util.print_log('your choice does not exist', 'error')