#!/usr/bin/env Python
# coding=utf-8

from methods.db import *

def select_table(table, column, condition, value):
    sql = "select " + column + " from " + table + " where " + condition + "='" + value + "'"
    print(sql)
    cur.execute(sql)
    lines = cur.fetchall()
    return lines

def add_table(table, key, value):
    sql = f"insert into {table} {key} values {value}"
    print(sql)
    cur.execute(sql)
    lines = conn.commit()
    return lines

def del_table(table, value):
    sql = f"delete from {table} where {value}"
    print(sql)
    cur.execute(sql)
    lines = conn.commit()
    return lines

def update_table(table, value, where):
    sql = f"UPDATE {table} SET {value} WHERE {where}"
    print(sql)
    cur.execute(sql)
    lines = conn.commit()
    return lines

def exec_sql(sql):
    cur.execute(sql)
    lines = cur.fetchall()
    return lines
