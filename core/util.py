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


# def com_tran_module(user_data,tran_type,):
#     """
#
#     :param user_data:
#     :return: user_info , and back_flag
#     """
#     user_info = db_handler.load_file(user_data['account_name'])#user_data 全局变量
#     balance_info = ''' --------- bank info --------
#             credit: %s
#             balance: %s''' % (user_info['credit'], user_info['balance'])
#
#     print_log(balance_info, 'info')
#     back_flag = False
#     while not back_flag:
#         if tran_type in settings.TRANSACTION_TYPE:
#             amount = input('please input the transaction amount>>:').strip()
#             if len(amount)>0 and amount.isdigit():
#                 amount = float(amount)
#                 if tran_type == 'transfer':
#                     transfer_name1 = input('please input the account you want to transfer>>:').strip()
#                     if transfer_name1 == 'b' or amount == 'b':
#                         return
#                     file_name = '%s/account/%s.json' % (settings.BASE_DIR, transfer_name1)
#                     if os.path.isfile(file_name):
#                         new_balance,save_flag = transaction.make_transaction(trans_logger, user_info, tran_type, amount, transfer_name = transfer_name1)
#                 else:
#                     new_balance, save_flag = transaction.make_transaction(trans_logger, user_info, tran_type, amount)
#                 if save_flag:
#                     util.print_log('transaction successfully', 'info')
#                     util.print_log('current balance>>%s' % new_balance['balance'], 'info')
#                 else:
#                     util.print_log('there is some thing wrong and the transaction is not success', 'error')
#
#             elif amount == 'b':
#                 back_flag = True
# #



# a = passwd_md5('luffy','1234')
# print(a)