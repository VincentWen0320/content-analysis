# encoding=utf-8
import numpy as np
import jieba.analyse
import sys
import re
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

#Note: Sentiment classification based on voting method

jieba.load_userdict("dict_ciku.txt")
f=open("szguba.txt").readlines()
wordlist=open("optimist_dict.txt").readlines()   #the file is saved by 'ANSI' style
wordlist1=open("pessimist_dict.txt").readlines()
NA=open("negation.txt").readlines()   # 13 negations with high frequency
r=open("classification.txt","w")  # output

newwordlist=[]
for word in wordlist:
    word=word.strip().decode('gbk', 'utf-8')
    newwordlist.append(word)

newwordlist1=[]
for word1 in wordlist1:
    word1=word1.strip().decode('gbk','utf-8')
    newwordlist1.append(word1)

newna=[]
for na in NA:
    na1=na.strip().decode('gbk','utf-8')
    newna.append(na1)

for sen in f:
    sen = sen.strip().decode('gbk','utf-8')
    segtmp = jieba.lcut(sen, cut_all=False)
    total=0

    for word in segtmp:
        i = 0
        a = 0
        poscount = 0
        poscount2 = 0
        poscount3 = 0
        negcount = 0
        negcount2 = 0
        negcount3 = 0
        if word in newwordlist:
            poscount += 1
            a = segtmp.index(word)
            i = a-4
            c = 0
            poscount3 = poscount
            if i < 0:
                i = 0

            for w in segtmp[i:a]:
                if w in newna:
                    c += 1
            if c%2==0:
                poscount3=poscount
            else:
                poscount2=-1.0*poscount
                poscount3=poscount2

        elif word in newwordlist1:
            negcount -= 1
            b = segtmp.index(word)
            j = b - 4
            d = 0
            negcount3 = negcount
            if j < 0:
                j = 0

            for w in segtmp[j:b]:
                if w in newna:
                    d += 1
            if d % 2 == 0:
                negcount3 = negcount
            else:
                negcount2 = -1.0 * negcount
                negcount3 = negcount2
        total= total + poscount3 + negcount3
        if total>0:
            total=1
        elif total<0:
            total=-1

    total=str(total)
    r.write(total)
    r.write('\r\n')
r.close()