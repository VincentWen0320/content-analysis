# encoding=utf-8
import jieba.analyse
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
import re

#Note: selecting the high-frequency words from messages.

jieba.load_userdict("dict_ciku.txt")    # dict_ciku.txt: the training set of words for segmentation
content1=open("szguba.txt").read()
tags=jieba.analyse.extract_tags(content1,topK=1200)
print u"关键词："
print" ".join(tags)
