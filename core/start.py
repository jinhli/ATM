#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/12/18

#https://www.cnblogs.com/zhengyuan/p/8454216.html
#用户验证登陆程序
import json
import time
import os
import hashlib
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)



def load_file(account):
    """
    :param account:
    :return: user_info
    :用户信息读到内存
    """
    # user_info = {} #可以不需要提前定义
    file_name = '%s/account/%s.json'%(BASE_DIR,account)
    if os.path.isfile(file_name):
        with open(file_name,'r',encoding='utf-8') as f:
            user_info = json.load(f)
            return user_info
    else:
        print_log('there is no account info for %s'%account,'error')
        exit()


# def update_file(account):
#     """
#     更新这里， 保证所有的修改都能使用
#     :param account:
#     :return: no return
#     用户信息更新到文件
#     """
#     user1_info = load_file(account)
#     user1_info['status'] = 1
#     file_name = '%s/account/%s.json'%(BASE_DIR,account)
#
#     with open(file_name,'w',encoding='utf-8') as f:
#         json.dump(user1_info,f)

def update_file(account,user_info):
    """
    更新这里， 保证所有的修改都能使用
    :param account:
    :return: no return
    用户信息更新到文件
    """
    file_name = '%s/account/%s.json'%(BASE_DIR,account)

    with open(file_name,'w',encoding='utf-8') as f:
        json.dump(user_info,f)

def access_auth(account,password):
    """

    :param account:
    :param password:
    :return: account_data
    """
    account_data =load_file(account)
    if account_data['status'] == 0:
        password_md5 = passwd_md5(account,password)
        if password_md5 == account_data['password']:
            expire_time = time.mktime(time.strptime(account_data['expire_date'],'%Y-%m-%d'))
            if time.time() > expire_time:
                print_log('the account %s has been expired, please contact the bank'%account,'error')
                exit()
            else:
                print_log('welcome %s \o/'%account,'info')
                return account_data
        else:
            print_log('the password of the account %s is not right'%account,'error')
    else:
        print_log('the account %s has been locked, please contac the bank'%account,'error')
        exit()


def passwd_md5(account,password):
    """

    :param account:
    :param password:
    :return:  MD5 密码
    """

    md5 = hashlib.md5(account.encode('utf-8'))#带上用户名加密
    md5.update(password.encode('utf-8')) #加上encode编码
    ret = md5.hexdigest()
    return ret

def user_login():
    """
    #登陆函数
    :return:
    """
    retry_count = 0
    while retry_count<3:
        account = input('please input your account->').strip()
        password = input('please input your password->').strip()
        load_file(account)
        account_data = access_auth(account,password)
        user_interface(account_data)
        retry_count+=1
    else:
        update_file(account)


def user_interface(account_data):
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
        '1':account_info,
        '2':'repay',
        '3':'withdraw',
        '4':'transfer',
        '5':'pay_check',
        '6':'logout',
    } # 函数字典， 实际上每个选项对应一个函数
    exit_flag = False
    while not exit_flag:
        print_log(menu,'info')
        user_option = input('>>:').strip()
        if user_option in menu_dic:
            menu_dic[user_option](account_data)
            # print(menu_dic[user_option]) #调用各功能功能
            # pass


def account_info(user_info,*args, **kwargs):
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
    print('ACCOUNT INFO'.center(50,'-'))
    for k,v in user_info['data'].items():  #???
        if k not in ('password',):
            print_log('%15s:%s'%(k,v))
        print('END'.center(50,'-'))

def repay(user_info):
    """
    还款
    :param user_info:
    :return:
    """
    pass


def transfer(user_info):
    """
    转账
    :param user_info:
    :return:
    """
    transfer_name = input('please input the account you want to transfer>>:').strip()
    transfer_amount = float(input('please input the amount>>:').strip())
    transfer_info = load_file(transfer_name)
    older_balance = user_info['balance']
    user_info['balance'] = older_balance-transfer_amount
    transfer_info['balance'] = float(transfer_info['balance']+transfer_amount)

    # print(user_info['balance'],transfer_info['balance'])
    update_file('luffy',user_info)
    update_file(transfer_name,transfer_info)

# def withdraw(user_info):
#     """
#     取现，取先利息是5%
#     :param user_info:
#     :return:
#     """"
#     withdraw_amount = float(input('please input the amount you want to '))


# def make_transaction(log_obj,account_data,tran_type,amount,**kwargs):
     '''
     处理所有用户的所有交易
     :param log_obj:
     :param account_data: 用户最新的数据
     :param tran_type: 交易类型
     :param amount: 交易数量
     :param other: 主要用于日志使用
     :return: 返回最新的账户数据
     '''


user_login()
#user_interface()



















