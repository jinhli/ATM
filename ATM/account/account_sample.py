#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/14/18
import json
import os
import sys
import datetime
from core import db_handler
from core import util
from core import main
from conf import settings
from core.auth import login_required

def add_acc():
    """
    :return:
    """
    acc_dic = {
        'id': 1234,
        'password': 'abc',
        'credit': 15000,
        'balance': 15000,
        'enroll_date': '2016-01-02',
        'expire_date': '2021-01-01',  # 自动开卡日期+5年
        'pay_day': 22,
        'status': 0, # 0 = normal, 1 = locked, 2 = disabled
        'admin_flag': 0  # 0 = not admin, 1 = admin
    }
    user_data1 = {'account_data':None}
    exit_flag = False
    while not exit_flag:
        acc_name = input('please input  name>>').strip()
        accout_file = '%s/account/%s.json' % (settings.BASE_DIR, acc_name)
        if os.path.isfile(accout_file):
            util.print_log('the account %s has been existed, please use a new name' %acc_name,'error')
            return
        else:
            password = input('please input more than 5 digists>>').strip()
            if (len(password)>= 5 and password.isdigit()):
                acc_dic['id'] = acc_name
                acc_dic['password'] = util.passwd_md5(acc_name, password)
                current_date = datetime.datetime.now() #注册日期
                expire_date = current_date + datetime.timedelta(1095) #到期日
                pay_day = current_date + datetime.timedelta(50) #还款日期
                acc_dic['enroll_date'] = current_date.strftime('%Y-%m-%d')     #2016-01-02
                acc_dic['expire_date'] = expire_date.strftime('%Y-%m-%d')
                acc_dic['pay_day'] = pay_day.day
                db_handler.update_file(acc_dic['id'],acc_dic)
                util.print_log('%s account has been created' % name, 'info')
                user_data1['account_data'] = acc_dic
                main.account_info(user_data1)
                exit_flag = True

            elif acc_name == 'b' or password == 'b':
                exit_flag = True
            else:
                util.print_log('please input the name and password again','error')





def lock_or_not(lock_flag):
    exit_flag = False
    while not exit_flag:
        acc_name = input('input the account you want to locked>>').strip()
        if acc_name == 'b':
            exit_flg = True
        else:
            accout_file = '%s/account/%s.json' % (settings.BASE_DIR, acc_name)
            if os.path.isfile(accout_file):
                acc_dic = db_handler.load_file(acc_name)
                if lock_flag == 1: #lock
                    acc_dic['status'] = 1 #lock
                else:
                    acc_dic['status'] = 0  #unlock
                db_handler.update_file(acc_dic['id'], acc_dic)
                return
            else:
                util.print_log('%s does not exist, please double check','error')


def unlock_acc():
    lock_flag = 0
    lock_or_not(lock_flag)
    return

def lock_acc():
    lock_flag = 1
    lock_or_not(lock_flag)
    return


def logout(): #想退出到上一层目录
    # return
    exit('exit the system')

def manage_main(user_data):
    """
    管理主程序
    :param user_info: 是个人信息字典
    :return:
    """

    adm_menu = u"""
        -------Administrator interface ---------
        1.Add new account
        2.Lock account 
        3.Unlock account
        4.Logout
        """
    menu_dic = {
        '1': add_acc,
        '2': lock_acc,
        '3': unlock_acc,
        '4': logout,
    }  #

    exit_flag = False
    while not exit_flag:
        util.print_log(adm_menu,'info')
        user_option = input('please input your choice>> ').strip()
        if user_option in menu_dic:
            menu_dic[user_option]()
        else:
            util.print_log('input the wrong choice, please try again','error')

#
# manage_main()