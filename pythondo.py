#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Filename:
# Author:    E-mail:qingant@gmail.com
# Lisence: GPL-2.0 
from  Tkinter import *
import os
import suggoogle



import urllib
import urllib2,re



    

def getpage(keyword):
    url = "http://suggestion.baidu.com/su?wd="
    URL= urllib.quote_plus(keyword.encode('utf-8'))

    print( URL,url)

    req = urllib2.Request(url+URL)
    print url+URL
    req.add_header( "Cookie" , "SUID=A1E7C8CA65590B0A49CA311E0006979E; ad=gZllllllll2Jh09Wlllll9odCiUlllllh70Xoyllll9lllllVqxlw@@@@@@@@@@@; IPLOC=CN6101; SUV=1245607601164169; JSESSIONID=abcoYYblt-KqFeXZ--dis" ) # 这里通过add_header方法很容易添加的请求头
    req.add_header( "User-Agent", "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008101315 Ubuntu/8.10 (intrepid) Firefox/3.0.11" )
    res = urllib2.urlopen( req )
    html = res.read().decode("gbk").encode('utf-8')
    res.close()
    print html
    return html

def getlist(page):
    p = re.compile(".*\[(.*)\].*")
    m = p.match(page)
    try :
        return eval(m.group(1))
    except :
        return False

def getsug(keyword):
    return getlist(getpage(keyword))











class SearchBar(Frame) :
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        entry=Entry(parent,width=40)
        entry.pack()
        #haha = ScrolledList(entry,root)
        self.entry = entry
        self.pos = 0
        entry.focus()
        entry.bind('<Return>',self.run())
        entry.bind('<Tab>',(lambda event:self.suggest()))
        entry.bind('<Escape>',(lambda event:self.quit()))
        #entry.bind('<Key>',self.onreturn)
        self.config(height=0)
        self.pack(fill=X)
        self.makeWidgets()
    def run(self):
        

        URL= urllib.quote_plus(self.entry.get().encode('utf8'))
        os.system("firefox http://www.google.cn/search\?hl=zh-CN\&q=\%s"%URL+' &')
        self.quit()
        pass
    def suggest(self):
    
        keywords = suggoogle.getsug(self.entry.get())
        self.makesug(keywords)
        print 'hahhhhhhhhhhhhhhhhhh'
        self.entry.focus()
        pass


            
            
        
     
    
        
   
    
    
    def handleList(self,event):
        index=self.listbox.curselection()
        label=self.listbox.get(index)
        self.runCommand(label)
    def makeWidgets(self):
#        sbar=Scrollbar(self)
        list=Listbox(self)
 #       sbar.config(command=list.yview)
        list.config(height=0,font=('Courier New',12,'bold'))
  #      sbar.pack(side=RIGHT,fill=Y)
        list.pack(side=LEFT,expand=YES,fill=X)
        
        list.bind('<Double-1>',self.handleList)
        list.bind('<Return>',self.handleList)
        self.listbox=list
#        self.sbar=sbar
    def makesug(self,keywords):
        self.pos=0
        self.listbox.delete(0,END)
        for label in keywords:
            self.listbox.insert(self.pos,label)
            self.pos += 1

    def runCommand(self,selection):
        print selection
        self.entry.delete(0,END)
        self.entry.insert(0,selection.encode('utf-8'))
        self.entry.focus()
        print 'focus'
        self.listbox.delete(0,END)
        self.pos = 0

        #        self.sbar.config(height=0)
        print 'haha'


class LaunchBar(SearchBar):
    def __init__(self):
        SearchBar.__init__(self)

    def run(self):
        os.system(self.entry.get()+' &')
    
    def suggest(self):
    
        keywords = self.tabcomand(self.entry.get())
        SearchBar.makesug(self,keywords)
        print 'hahhhhhhhhhhhhhhhhhh'
        self.entry.focus()
        pass
    def tabcomand(self,word):
        
        def getcmdlist() :
            pathlist = os.popen("echo $PATH").read()[:-1].split(':')
            cmdlist = reduce(lambda x,y:x+y,[os.listdir(x) for x in pathlist])
            return cmdlist


        def search(input,cmdlist):
            p=re.compile(input+'.*')
            return [x for x in cmdlist if p.match(x)]
        return search(word,getcmdlist())




if __name__=='__main__' :
    LaunchBar().mainloop()
