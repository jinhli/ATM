#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/19/18

import os
import json
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #整个程序的主目录
sys.path.append('%s/ATM' %BASE_DIR)


from core import util
from core import logger


consume_logger = logger.logger('consume') #消费日志
product_file = '%s/shopping_mall/product_list.json' %BASE_DIR
user_file = '%s/shopping_mall/shopping_list.json' %BASE_DIR


def load_product():
    """
    #从文件中读取用户信息
    :return: product_list
    """
    if os.path.isfile(product_file):
        with open(product_file, 'r') as f:
            product_list = json.load(f) #货物信息是字典
    return product_list  #返回货物清单


def load_shop_cart():
    """
    # 从文件中读取购物信息
    :return: user_list
    """
    if os.path.isfile(user_file):
        with open(user_file,'r') as f1:
            user_shop_cart = json.load(f1)
    return user_shop_cart  #返回所有用户信息


def dump_account(user_shop_cart):
    """
    购物后信息存入到文档
    :param user_name:
    :return:
    """
    # user_list = load_account()
    if os.path.isfile(user_file):
        with open('%s.new' %user_file,'w') as f2:
            json.dump(user_shop_cart,f2)
        os.rename('%s.new' %user_file, user_file)
        return True


def print_good_balance(name, total_consume, shop_cart):
    user_shop_info = u"""
                -------welcom %s ---------
                1.  Total consume:%s
                2.  Product you have bought:%s
                """ % (name, total_consume, shop_cart)

    util.print_log(user_shop_info, 'info')


def shopping(name,log_obj):

    user_shop_cart = load_shop_cart()  # 所有用户的字典信息
    product_list = load_product()  # 所有货物清单
    shop_cart = []
    # original_balance = user_data['account_name']['balance'] # 加到main函数里
    consume_amount = 0
    exit_flag1 = False
    while not exit_flag1:
        good_num = [] #用来存商品名
        for index, k in enumerate(product_list):
            good_num.append(k)
            util.print_log("%s:%s-->price:%s" % (index, k, product_list[k]), 'info')
        num = input('if you want buy anything, input the good number, or input "b">>:').strip()
        if num.isdigit():  # 判断是否是数字
            num = int(num)
            if 0 <= num <= len(product_list):
                selected_good = good_num[num]
                good_price = product_list[selected_good]
                shop_cart.append(selected_good)
                user_shop_cart[name]['shop_cart'].append(selected_good)
                consume_amount = float(consume_amount) + float(good_price) #总共消费的金额
                util.print_log(
                        'you have choose %s, and the total money is %s' % (shop_cart, consume_amount),
                        'info')
        elif num.lower() == 'b':
            exit_flag = True
            print_good_balance(name, consume_amount, shop_cart)
            log_obj.info('account_name:%s, have bought %s,and the total cost:%s' % (name,shop_cart,consume_amount))
            dump_account(user_shop_cart)
            return consume_amount
        else:
            print('The good does not exist')







# shopping('huahua',consume_logger)

