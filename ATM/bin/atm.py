#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/14/18


import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #整个程序的主目录
sys.path.append(BASE_DIR)


from core import main

# consume_logger = logger.consume_logger(name)

if __name__ == '__main__':
    main.run()


