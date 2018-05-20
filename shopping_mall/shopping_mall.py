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
# print(BASE_DIR)
# print(sys.path)
from core import util
from core import logger
from core import pay_check

#临时账户
user_data = {
    'account_name': None,
    'is_authenticated': False,
    'account_data': None

}

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
    return product_list #返回货物清单


def load_account():
    """
    # 从文件中读取购物信息
    :return: user_list
    """
    if os.path.isfile(user_file):
        with open(user_file,'r') as f1:
            user_list = json.load(f1)
    return user_list#返回所有用户信息


user_list = load_account()  # 所有用户的字典信息
product_list = load_product()  # 所有货物清单


def dump_account(user_list, user_name):
    """
    购物后信息存入到文档
    :param user_name:
    :return:
    """
    # user_list = load_account()
    if os.path.isfile(user_file):
        with open('%s.new' %user_file,'w') as f2:
            json.dump(user_list,f2)
        os.rename('%s.new' %user_file, user_file)
        return True


def print_good_balance(name, current_balance, shop_cart, shop_time):
    user_shop_info = u"""
                -------welcom %s ---------
                1.  current balance:%s
                2.  Product you have bought:%s %s
                """ % (name, current_balance, shop_cart, shop_time)

    util.print_log(user_shop_info, 'info')


def recharge(user_list, name, log_obj):
    current_balance = user_list[name]['balance']
    salary = input('Do you want to recharge your account, if "Yes",input the amount, if "No",input "b">>:').strip()
    if salary == 'b':
        util.print_log('you did not recharge any money', 'info')
    elif len(salary) > 0 and salary.isdigit():
        current_balance = float(salary) + float(current_balance)
        user_list[name]['balance'] = current_balance
        dump_account(user_list, name)
        # print('current_balance is %s' %current_balance,)
    util.print_log('current_balance is %s' % current_balance, 'info')
    exit_flag1 = False
    shop_cart = []
    original_balance = current_balance
    while not exit_flag1:
        good_num = []
        for index, k in enumerate(product_list):
            good_num.append(k)
            util.print_log("%s:%s-->price:%s" % (index, k, product_list[k]), 'info')
        num = input('if you want buy anything, input the good number, or input "b">>:').strip()
        if num.isdigit():  # 判断是否是数字
            num = int(num)
            if 0 <= num <= len(product_list):
                selected_good = good_num[num]
                good_price = product_list[selected_good]

                if float(good_price) > float(user_list[name]['balance']):  # 钱不够
                    # print('Sorry, your salary could not afford %s' %selected_good)
                    util.print_log('Sorry, your salary could not afford %s' % selected_good, 'error')
                    credit_or_not = input(
                        'Do you want to use the credit card to buy the product, if "yes",input "y",or input "n">>').strip()
                    if credit_or_not == 'y':

                    elif credit_or_not == 'n':
                        util.print_log("you can continue to choose other goods", 'info')
                else:
                    shop_cart.append(selected_good)
                    user_list[name]['shop_cart'].append(selected_good)
                    user_list[name]['balance'] = float(user_list[name]['balance']) - float(good_price)

                    # print('you bought %s, and the current balance is %s' %(selected_good,user_list[name]['balance']))
                    util.print_log(
                        'you bought %s, and the current balance is %s' % (selected_good, user_list[name]['balance']),
                        'info')
        elif num.lower() == 'b':
            exit_flag = True
            cost_amount = float(original_balance) - float(user_list[name]['balance'])
            print_good_balance(name, user_list[name]['balance'], shop_cart, 'today')
            log_obj.info('account_name:%s, have bought %s,and the total cost:%s' % (
                name, shop_cart, cost_amount))
            dump_account(user_list, name)

            exit('quit the shopping_mall')
        else:
            print('The good does not exist')



def shopping_mall():
    """

    :return:
    """

    try_count = 0
    while try_count <3:
        name = input('input your name:').strip()
        passwd = int(input('input your password:').strip())
        if name in user_list and passwd == user_list[name]['password']:
            current_balance = user_list[name]['balance']
            shop_cart= user_list[name]['shop_cart']
            print_good_balance(name, current_balance, shop_cart,'history')
            # user_shop_info = u"""
            # -------welcom %s ---------
            # 1.  current balance:%s
            # 2.  Product you have bought:%s
            # """ %(name, current_balance,shop_cart)
            # # print(user_shop_info)
            # util.print_log(user_shop_info, 'info')
            recharge(user_list, name,consume_logger)

        else:
            try_count +=1
            # print('incorrect password or name,please try again')
            util.print_log('incorrect password or name,please try again','error')
            if try_count == 3:
                exit('you have try 3 times')





shopping_mall()

