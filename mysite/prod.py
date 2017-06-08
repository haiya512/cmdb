#!/usr/bin/env python
# -*- coding: utf-8 -*-

DEBUG = True
website = "http://127.0.0.1"

pxe_url_api = "http://192.168.115.180:8888/clone/"

# salt api config
salt_api_url = "https://127.0.0.1/"
salt_api_user = "admin"
salt_api_pass = "admin"

Environment = ['prod', 'beta', 'dev', 'st', 'qa']

# salt auth
auth_content = ['vi', 'vim',
                'poweroff', 'shutdown', 'reboot', 'init',
                'rm', 'useradd', 'userdel', 'userhelper',
                'usermod', 'usernetctl', 'users', "echo"]

# LOGIN_URL = "http://auth.jumeird.com/api/login/?camefrom=jmops"
app_key = "&app_key=e00acc666d4911e3a268fa163e73f605"
app_name = "&app_name=jmops&key=1"
auth_url = "http://auth.xxx.com/"
auth_key = "e00acc666d4911e3a268fa163e73f605"

# 跳板机使用
springboard = "ea76757b5d91c5c96bf58500a5f7eda0"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cmdb_v2',
        'USER': 'root',
        'PASSWORD': 'centos',
        # 'PASSWORD': 'Ubp-ndv7tNphiwut5ora',
        'HOST': '192.168.1.102',
        'PORT': '3306',
        "OPTIONS": {
            "init_command": "SET foreign_key_checks = 0;",
        },
    },
}

# from pymongo import MongoClient
# client = MongoClient('localhost',27017)
# db = client['config_center']

# salt tornado api
# salt_tornado_api = "http://10.1.2.21:8888/api/"

swan_url = "http://127.0.0.1:8888/swan_api/"
# swan_url = "http://192.168.115.205/swan_api/"

websocket_url = "127.0.0.1:8888/websocket"
# websocket_url = "ops.int.funshion.com/websocket"
ops_mail = "voilet@qq.com"
