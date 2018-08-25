# -*- coding: utf-8 -*-
"""
import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost:8889',
    'database': 'GAME',
    'raise_on_warnings': True,
}

link = mysql.connector.connect(**config)
"""
"""
import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
    'database': 'GAME',
    'raise_on_warnings': True,
}

link = mysql.connector.connect(**config)

try:
    with link.cursor() as cursor:
        sql = "SELECT * FROM mygame"
        cursor.execute(sql)
        
        dbdata = cursor.fetchall()
        for rows in dbdata:
            print(rows)

finally:
    link.close()
"""
"""
from urllib.parse import urlparse
import mysql.connector

url = urlparse('mysql://user:pass@localhost:8889/GAME')

conn = mysql.connector.connect(
                               host = url.hostname or 'localhost',
                               port = url.port or 8889,
                               user = url.username or 'root',
                               password = url.password or 'root',
                               database = url.path[1:],
                               )

conn.is_connected()
"""
"""
import mysql.connector

conn = mysql.connector.connect(user='root',
                               password='root',
                               host='localhost',
                               database='sample')
cur=conn.cursor()
"""
"""
import MySQLdb

conn = MySQLdb.connect(
                            unix_socket = '/Applications/MAMP/tmp/mysql/mysql.sock',
                            host='localhost', user='root', passwd='root', db='GAME'
                            )

cursor = conn.cursor()
try:
    cursor.execute('select * from mygame')
    result = cursor.fetchall()
finally:
    cursor.close()
    conn.close()
"""
"""
import mysql.connector

def m():
    cnt = mysql.connector.connect(
                                  host='localhost',
                                  port='8889',
                                  db='GAME',
                                  user='root',
                                  password='root',
                                  charset='utf8'
                                  )

    db = cnt.cursor()

    
    sql = 'SELECT 名前 FROM mygame';
    db.execute(sql)

    rows = db.fetchall()

    for i in rows:
        print(i[0])
    
    db.close()
    cnt.close()

if __name__ == '__main__':
    m()
"""
import MySQLdb

def m():
    cnt = MySQLdb.connect(
                                host='localhost',
                                port='8889',
                                db='GAME',
                                user='root',
                                password='root',
                                charset='utf8'
                         )
    """
    db = cnt.cursor()

    sql = 'SELECT 名前 FROM mygame';
    db.execute(sql)
    rows = db.fetchall()
    for i in rows:
        print(i[0])
        
    db.close()
    cnt.close()
    """
if __name__ == '__main__':
    m()
