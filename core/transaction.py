#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/14/18

from conf import settings
from core import logger
from core import db_handler


def make_transaction(log_obj, user_info, tran_type, amount, **kwargs):
    """
    处理所有的用户交易
    :param log_obj: log 类型
    :param user_info: 用户数据
    :param tran_type: 交易类型
    :param ammount: 交易数额
    :param kwargs: 以后扩展
    :return: 最新的用户数据
    """
    amount = float(amount)

    if tran_type in settings.TRANSACTION_TYPE :
        interest = amount * settings.TRANSACTION_TYPE[tran_type]['interest']
        old_balance = user_info['balance']
        # repay
        if settings.TRANSACTION_TYPE[tran_type]['action'] == 'plus':
            new_balance = old_balance + amount + interest
        # withdraw/transfer
        elif settings.TRANSACTION_TYPE[tran_type]['action'] == 'minus':
            new_balance = old_balance - amount - interest
            # only for transfer
            if kwargs.get('transfer_name'):
                transfer_name_info = db_handler.load_file(kwargs.get('transfer_name'))
                transfer_name_balance = transfer_name_info['balance'] + amount
                transfer_name_info['balance'] = transfer_name_balance
                db_handler.update_file(transfer_name_info['id'], transfer_name_info)




