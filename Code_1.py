# -*- coding:utf-8 -*-
import requests
import random
import urllib
import urllib2
import re
import codecs

#Note: extracting the messages listed on Chinese stock message board Guba Eastmoney.

page = 1
f = codecs.open('szguba.txt', 'a', 'utf-8')  #file name
while page <= 800:
    url = 'http://guba.eastmoney.com/list,zssh000001,f_' + str(page)+'.html?from=BaiduAladdin'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    headers = { 'User-Agent' : user_agent }
    try:
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        pattern = re.compile(r'<div class="articleh">.*?<span class="l1">(.*?)</span><span class="l2">.*?<span class="l3"><a href=".*?.html" title="(.*?)" >.*?</a></span><span class="l4">.*?<span class="l6">(.*?)</span>',re.S)
        items = re.findall(pattern, content)
        print items
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason
    page+=1
f.close()

