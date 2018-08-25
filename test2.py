# -*- coding: utf-8 -*-
import sys
import MeCab
import pandas as pd
import mysql.connector


def livedoor_file_open():
    file_name = "/Users/itorinta/Desktop/python研究/単純ベイズ分類器/dokujo-tsushin-4778030.txt"
    try:
        file = open(file_name)
        data = file.read()
    #print(data)
    except Exception as e:
        print(e)
    finally:
        file.close()
        return data

def wakati_by_mecab(text):
    #db(MySQL接続)
    cnt = mysql.connector.connect(
                                  host='localhost',
                                  port='8889',
                                  db='word_livedoor',
                                  user='root',
                                  password='root',
                                  charset='utf8'
                                  )
    db = cnt.cursor()

    tagger = MeCab.Tagger('')
    tagger.parse('')
    node = tagger.parseToNode(text) #形態素解析実行
    word_list = []
    while node:
        pos = node.feature.split(",")[0]
        if pos in ["名詞", "動詞", "形容詞"]:   # この3つの品詞のみを格納
            word = node.surface #単語のみを抽出
            word_list.append(word)
            resultx = node.feature
            db = cnt.cursor()
            sql1 = 'insert into word_livedoor.word_information (word, result) values (%s, %s);'
            data_mysql = (word, resultx)
            db.execute(sql1, data_mysql)
        node = node.next #次の単語へ
    sql2 = 'SELECT word FROM word_information';
    db.execute(sql2)
    rows = db.fetchall()
    for i in rows:
        print(i[0])
    db.close()
    cnt.commit()
    cnt.close()
    return " ".join(word_list)

if __name__ == '__main__':
    text = livedoor_file_open() #ファイルを開く
    result = wakati_by_mecab(text) #形態素解析（分かち書き）
    
    #list = result.split(' ') #単語ごとにlistに格納
    #print(result)
    #lisr表示
    """
        for i in list:
            print(i)
    """
