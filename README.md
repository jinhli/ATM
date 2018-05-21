作者:Bonnie Li
版本:示例版本 v0.1
程序介绍:
    实现ATM常用功能 + 购物商场（购物功能集成在ATM里）
    用到的函数知识点：
    time\os\sys\json\open\logging\re\MD5\函数装饰器\模块知识

程序结构:
credit_card_1.
├── ATM
│   ├── account  #ATM 账户信息
│   │   ├── hanhan.json
│   │   ├── huahua.json
│   │   ├── __init__.py
│   │   └── luffy.json
│   ├── bin #主执行程序
│   │   ├── atm.py #运行atm.py执行程序
│   │   └── __init__.py
│   ├── conf #配置文件目录
│   │   ├── __init__.py
│   │   └── settings.py 
│   ├── core
│   │  
│   │   ├── auth.py #用户认证模块
│   │   ├── db_handler.py #数据加载和保存
│   │   ├── __init__.py
│   │   ├── logger.py #日志记录
│   │   ├── main.py #主程序
│   │   ├── manage.py #管理员模块
│   │   ├── transaction.py #交易处理模块
│   │   └── util.py # 打印 和MD5 模块
│   ├── __init__.py
│   └── log #各种日志
│       ├── access.log #登陆日志
│       ├── consume.log #暂时没用
│       ├── hanhan.log
│       ├── huahua.log
│       ├── __init__.py
│       ├── luffy.log #以人名命名的日志是消费流水
│       └── transactions.log #交易日志，主要还款，取现，转账，消费
├── __init__.py
├── README.md
└── shopping_mall
    ├── __init__.py
    ├── product_list.json #商品记录
    ├── shopping_list.json#用户购买记录
    └── shopping_mall.py #用户购买商品模块
程序简单使用说明：
luffy ->管理员兼普通用户，用户密码 1234
hanhan ->普通用户，用户密码 1234

所有的步骤都可以通过输入“b”退回到上层菜单
