import MeCab
import string
import sys
"""
class NaiveBayes():
    def livedoor_file_open():
        file_name = "/Users/itorinta/Desktop/python研究/単純ベイズ分類器/dokujo-tsushin-4778030.txt"
        try:
            file = open(file_name)
            data = file.read()
            print(data)
        except Exception as e:
            print(e)
        finally:
            file.close()
            return data

    def wakati(file_data):
        tagger = MeCab.Tagger('-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
        wakati = tagger.parse(file_data)
        wakati_result = wakati.split(' ')
        tango = []
        for i in wakati_result:
            print(i)
            if i == '\n':
                break
            tango.append(i)
            #print(tango)

if __name__ == '__main__':
    NB = NaiveBayes()
    livedoor_file_data = NB.livedoor_file_open()
    NB.wakati(livedoor_file_data)
"""

# ファイル読み込み
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

# 分かち書き（形態素解析）
def wakati(file_data):
    # mecab-ipadic-neologdという辞書を使用
    #tagger = MeCab.Tagger('-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    tagger = MeCab.Tagger('-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    tagger.parse('')
    wakati = tagger.parseToNode(file_data)
    """
    wakati_result = wakati.split(' ') # 単語ごとに改行
    #wakati_result = wakati.rsplit('\n') # 単語ごとに空白
    tango = []
    
    for i in wakati_result:
        print(i)
        if i == '\n':
            break
        tango.append(i)
#print(tango)
"""
    while wakati:
        print('%-10s \t %-s' % (wakati.surface, wakati.feature))
        wakati = wakati.next

if __name__ == '__main__':
    livedoor_file_data = livedoor_file_open()
    wakati(livedoor_file_data)

