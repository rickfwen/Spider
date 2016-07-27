# coding=utf-8
import urllib2
import re
import thread
import time
import re
from HTMLParser import HTMLParser 
import wikipedia
import sys

class MyHTMLParser(HTMLParser):

  def __init__(self):
    HTMLParser.__init__(self)
    self.recording = 0 
    self.data = []
  
  #??hashtag   
  def handle_starttag(self, tag, attrs):
    if tag == 'table':
      #if name == "href":
      #    print name, "=", value
      a=0
      b=0
      for name, value in attrs:
        if name == 'class' and value == 'wikitable':
          a=1
          print name, value
        if name == 'style' :
          b=1
          print name, value
        if a==1 and b==1:
          self.recording = 1  


  def handle_endtag(self, tag):
    if tag == 'table':
      self.recording -=1 

  def handle_data(self, data):
    if self.recording:
      self.data.append(data)

class Spider_Wiki:

    def __init__(self):    
        self.page = 1    
        self.pages = []    
        self.enable = False
        self.preUrl='https://zh.wikipedia.org/wiki/'
        #???????
        self.pageLocalLeader='%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E7%9C%81%E7%BA%A7%E8%A1%8C%E6%94%BF%E5%8C%BA%E9%A2%86%E5%AF%BC%E4%BA%BA'
        #???????
        self.pageCentralLeader='%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E7%9C%81%E7%BA%A7%E8%A1%8C%E6%94%BF%E5%8C%BA%E9%A2%86%E5%AF%BC%E4%BA%BA'

#Leadership Mother 
    def GetMotherPage(self): 
        #?????   
        myUrlLocal = self.preUrl + self.pageLocalLeader
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'   
        headers = { 'User-Agent' : user_agent }   
        req = urllib2.Request(myUrlLocal, headers = headers)   
        myResponse = urllib2.urlopen(req)  
        myPage = myResponse.read()    
 
        unicodePage = myPage.decode("utf-8")    

        
        p = MyHTMLParser()
        #???????
        p.feed(myPage)
        #???d?test??
        with open(r'D:\structure.txt', 'wb') as OUTFILE:
            for item in p.data:
                OUTFILE.write(item)

        #Work in progress: Function GetChildPage
        #Example: Get the href and store it with the data
        #<td><a href="/wiki/%E5%8C%97%E4%BA%AC%E5%B8%82" title="???">???</a></td>
        #<td><a href="/wiki/%E9%83%AD%E9%87%91%E9%BE%99" title="???">???</a></td>
        #<td><a href="/wiki/%E6%9D%9C%E5%BE%B7%E5%8D%B0" title="???">???</a></td>
        #<td><a href="/wiki/%E7%8E%8B%E5%AE%89%E9%A1%BA" title="???">???</a></td>
        #<td><a href="/wiki/%E5%90%89%E6%9E%97_(%E4%BA%BA%E7%89%A9)" title="?? (??)">???</a></td>
        print u'Mother Page Done' 
    
    def GetChildPage(self,page):
        #In Child Page get the ??  as same structure in wikitable

        print 'a'


    def LoadPage(self):    
        while self.enable:    
            try:    
                myPage = self.GetPage()    
                self.page += 1    
                self.pages.append(myPage)
            #????        
            except Exception as e :    
                print e  
  
            
    def Start(self):    
        self.enable = True    
        page = self.page    
    
        print u'Loading Pages'    
            
        
        self.GetMotherPage()    
            
        while self.enable:    
            if self.pages:    
                nowPage = self.pages[0]    
                del self.pages[0]    
                page += 1    


#----------- Entry-----------    
reload(sys)
sys.setdefaultencoding("utf-8")
myModel = Spider_Wiki()    
myModel.Start()    

