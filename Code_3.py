#encoding=utf-8
import re
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

#Note: calculating the frequency of each high-frequency word

f=open("szguba.txt").readlines()
wordlist=open("high-frequency words.txt").readlines()   #the file is saved by 'ANSI' style

total = f.__len__()
px=open("frequency.txt","w")
for word in wordlist:
    word=word.strip().decode('gbk', 'utf-8')
    count=0
    for doc in f:
        doc=doc.strip().decode('gbk', 'utf-8')
        if re.search(word,doc):
            count+=1

    percent = format(float(count) / total, '.6f')
    px.write(word)
    px.write(',')
    px.write(percent)
    px.write('\r\n')
    print word
    print count

px.close()
print total
