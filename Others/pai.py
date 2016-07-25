1 # coding=utf-8
import urllib2
import re
import thread
import time
import re

  
preUrl='https://zh.wikipedia.org'
#Leadership Mother Page
provinceUrl='https://zh.wikipedia.org/wiki/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E7%9C%81%E7%BA%A7%E8%A1%8C%E6%94%BF%E5%8C%BA%E9%A2%86%E5%AF%BC%E4%BA%BA'
loca='/Users/landanhu/Desktop/abc.html'
7 
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urldata = opener.open(provinceUrl)
f=file(loca,'w')
m=urldata.read()
print>>f,m