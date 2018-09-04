
# -*- coding: utf-8 -*-
import sys
import MeCab
import pandas as pd
#import pandas.io.sql as psql
import mysql.connector
import re
import urllib.request
import bs4
from bs4 import BeautifulSoup

#ファイルオープン
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

#ファイル内容を整える
def clean_text(text):
    replaced_text = '\n'.join(s.strip() for s in text.splitlines()[2:] if s != '')  # skip header by [2:]
    replaced_text = replaced_text.lower()
    replaced_text = re.sub(r'[【】]', ' ', replaced_text)       # 【】の除去
    #replaced_text = re.sub(r'[（）()]', ' ', replaced_text)     # （）の除去
    replaced_text = re.sub(r'[［］\[\]]', ' ', replaced_text)   # ［］の除去
    replaced_text = re.sub(r'[@＠]\w+', '', replaced_text)  # メンションの除去
    replaced_text = re.sub(r'https?:\/\/.*?[\r\n ]', '', replaced_text)  # URLの除去
    replaced_text = re.sub(r'　', ' ', replaced_text)  # 全角空白の除去
    return replaced_text

#ストップワード取得
def get_stop_words():
    #stopwords(文章の属性に関わらず頻出する単語)を除外するために、slothlibの日本語ようストップワードリストを取得。
    #urllibとBeautifulSoupによりソースをパース。
    url = 'http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'
    soup = bs4.BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
    ss = str(soup)
    return ss

#形態素解析
def wakati_by_mecab(text, stopword):
    tagger = MeCab.Tagger('')
    tagger.parse('')
    node = tagger.parseToNode(text) #形態素解析実行
    word_list = []
    while node:
        pos = node.feature.split(",")[0]
        if pos in ["名詞", "動詞", "形容詞"]:   # この3つの品詞のみを格納
            word = node.surface #単語のみを抽出
            if not word in stopword:
                word_list.append(word)
                word2 = node.surface
                resultx = node.feature
            sql1 = 'insert into word_livedoor.word_information (word2, result) values (%s, %s);'
            data_mysql = (word2, resultx)
            db.execute(sql1, data_mysql)
        node = node.next #次の単語へ
    sql2 = 'SELECT word FROM word_information';
    db.execute(sql2)
    rows = db.fetchall()
    """
    for i in rows:
    print(i[0])
    """
    db.close()
    cnt.commit()
    cnt.close()
    return " ".join(word_list)

def stopword_derete(text, stopword):
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



if __name__ == '__main__':
    text = livedoor_file_open() #ファイルを開く
    text_clean = clean_text(text)
    #print(text_clean)
    stop = get_stop_words()
    #print(stop)
    result = wakati_by_mecab(text_clean, stop) #形態素解析（分かち書き）
    
    #list = result.split(' ') #単語ごとにlistに格納
    print(result)
    #lisr表示
    """
        for i in list:
        print(i)
        """
    
    cnt = mysql.connector.connect(
                                  host='localhost',
                                  port='8889',
                                  db='word_livedoor',
                                  user='root',
                                  password='root',
                                  charset='utf8'
                                  )
                                  db = cnt.cursor()
                                  
                                  sql = 'select word, result from word_information'
                                  #sql = 'DELETE FROM word_information;'
                                  df = pd.read_sql_query(sql, cnt) # pandasのDataFrameの形でデータを取り出す
                                  cnt.close()
#df1['word'] = df['word'].apply( ) #カラム[word]に単語追加
#print(df['word'])
