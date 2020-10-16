#encoding=utf-8
import re
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

#Note: calculating the frequency that word_x and word_y co-occur

f=open("szguba.txt").readlines()
wordlist=open("uncertain_dict.txt").readlines()   #the file is saved by 'ANSI' style
wordlist1=open("pessimist_dict.txt").readlines()  #pessimist sentiment words are saved in 'pessimist_dict.txt'.
total = f.__len__()
pxy=open("P(x,y)1.txt","w")
for word in wordlist:
    word=word.strip().decode('gbk', 'utf-8')
    newwordlist=[]
    for doc in f:
        doc=doc.strip().decode('gbk', 'utf-8')
        if re.search(word,doc):
            newwordlist.append(doc)

    for word1 in wordlist1:
        word1=word1.strip().decode('gbk', 'utf-8')
        count=0
        for doc in newwordlist:
            if re.search(word1,doc):
                count+=1

        if count==0:
            percent = format(float(count+1) / (total+2), '.6f')
        else:
            percent = format(float(count) / total, '.6f')

        pxy.write(word)
        pxy.write(word1)
        pxy.write(',')
        pxy.write(percent)
        pxy.write('\r\n')
pxy.close()
