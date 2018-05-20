#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/14/18

from conf import settings
from core import logger
from core import db_handler
from core import util


def make_transaction(log_obj, user_info, tran_type, amount, **kwargs):
    """
    处理所有的用户交易
    :param log_obj: log 类型
    :param user_info: 用户数据
    :param tran_type: 交易类型
    :param amount: 交易数额
    :param kwargs: 以后扩展
    :return: 最新的用户数据
    """
    amount = float(amount)

    if tran_type in settings.TRANSACTION_TYPE:
        interest = amount * settings.TRANSACTION_TYPE[tran_type]['interest']
        old_balance = user_info['balance']
        #repay
        if settings.TRANSACTION_TYPE[tran_type]['action'] == 'plus':
            new_balance = old_balance + amount + interest
            log_obj.info('account_name:%s,transaction:%s,amount:%s,interest:%s' % (user_info['id'], tran_type, amount, interest))
        # withdraw/transfer/consume
        elif settings.TRANSACTION_TYPE[tran_type]['action'] == 'minus':
            new_balance = old_balance - amount - interest
            if new_balance < 0:
                util.print_log('there is no enough money to pay for the transition[-%s],you current balance is %s' % (amount, old_balance), 'error')
                save_flag = False
                new_balance = old_balance
                return new_balance,save_flag
            else:
                if kwargs.get('transfer_name'):  #only for transfer
                    transfer_name_info = db_handler.load_file(kwargs.get('transfer_name'))
                    transfer_name_balance = transfer_name_info['balance'] + amount
                    transfer_name_info['balance'] = transfer_name_balance
                    db_handler.update_file(transfer_name_info['id'], transfer_name_info)
                    log_obj.info('account_name:%s,transaction:%s,transfer_name:%s,amount:%s,interest:%s' % (
                    user_info['id'],tran_type,transfer_name_info['id'], amount, interest))
                    log_obj.info('account_name:%s,transaction:%s,transfer_name:%s,amount:%s' % (transfer_name_info['id'],
                    tran_type, user_info['id'], amount))
                else:
                    log_obj.info('account_name:%s,transaction:%s,amount:%s,interest:%s' % (
                    user_info['id'], tran_type, amount, interest))
        user_info['balance'] = new_balance
        save_flag = db_handler.update_file(user_info['id'], user_info) #数据保存成功
        return user_info,save_flag
    else:
        util.print_log('there is no %s transition type', tran_type)





