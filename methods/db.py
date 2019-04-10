#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", passwd="password", db="property", port=3306, charset="utf8")    #连接对象

cur = conn.cursor()    #游标对象
