1 # coding=utf-8
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
  def handle_starttag(self, tag, attrs):
    if tag == 'table':
      for name, value in attrs:
        if name == 'class' and value == 'wikitable':
          print name, value
          print "Encountered the beginning of a %s tag" % tag 
          self.recording = 1 


  def handle_endtag(self, tag):
    if tag == 'table':
      self.recording -=1 
      print "Encountered the end of a %s tag" % tag 

  def handle_data(self, data):
    if self.recording:
      self.data.append(data)

class Spider_Wiki:

    def __init__(self):    
        self.page = 1    
        self.pages = []    
        self.enable = False
        self.preUrl='https://zh.wikipedia.org/wiki/'
        self.page='%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E7%9C%81%E7%BA%A7%E8%A1%8C%E6%94%BF%E5%8C%BA%E9%A2%86%E5%AF%BC%E4%BA%BA'

#Leadership Mother 
    def GetPage(self,page):    
        myUrl = self.preUrl + self.page
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'   
        headers = { 'User-Agent' : user_agent }   
        req = urllib2.Request(myUrl, headers = headers)   
        myResponse = urllib2.urlopen(req)  
        myPage = myResponse.read()    
 
        unicodePage = myPage.decode("utf-8")    

        
        p = MyHTMLParser()
        p.feed(myPage)
        with open(r'D:\test.txt', 'wb') as OUTFILE:
            for item in p.data:
                OUTFILE.write(item)
        print p.data    




        #myItems = re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>',unicodePage,re.S)    
        #items = []    
        #for item in myItems:    
        #    # item ?????div?????????    
        #    # item ?????div?????????    
        #    items.append([item[0].replace("\n",""),item[1].replace("\n","")])    
        return items   

    # ????????    
    def LoadPage(self):    
        # ???????quit?????    
        while self.enable:    
            # ??pages????????2?    
            if len(self.pages) < 2:    
                try:    
                    # ???????????    
                    myPage = self.GetPage(str(self.page))    
                    self.page += 1    
                    self.pages.append(myPage)    
                except Exception as e :    
                    print e  
            else:    
                time.sleep(1)    
            
    def ShowPage(self,nowPage,page):    
        for items in nowPage:    
            print u'?%d?' % page , items[0]  , items[1]    
            myInput = raw_input()    
            if myInput == "quit":    
                self.enable = False    
                break    
            
    def Start(self):    
        self.enable = True    
        page = self.page    
    
        print u'Loading Pages'    
            
        # ????????????????    
        thread.start_new_thread(self.LoadPage,())    
            
        #----------- ???????? -----------    
        while self.enable:    
            # ??self?page???????    
            if self.pages:    
                nowPage = self.pages[0]    
                del self.pages[0]    
                self.ShowPage(nowPage,page)    
                page += 1    


#----------- ?????? -----------    

reload(sys)
sys.setdefaultencoding("utf-8")
myModel = Spider_Wiki()    
myModel.Start()    

