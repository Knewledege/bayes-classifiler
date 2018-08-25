# -*- coding: utf-8 -*-
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
