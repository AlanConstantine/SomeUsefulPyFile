# -*- coding: utf-8 -*-
# @Date     : 2017-05-08 11:05:05
# @Author   : Alan Lau (rlalan@outlook.com)
# @Language : Python3.5


import sqlite3


def connectSqlite(dbpath, sql):
    try:
        conn = sqlite3.connect(dbpath)
        cursor = conn.execute(sql)
        # conn.close()
        return cursor
    except Exception as e:
        print(e)
        raise
    else:
        pass
    finally:
        pass
