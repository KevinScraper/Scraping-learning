
from urllib.request import urlopen
from bs4 import BeautifulSoup 


html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs4Object = BeautifulSoup(html)
html.close()

"""""""""""""""""""""""""""""""""""""""""""""""""""""
bs4Object.findAll(tag, attributes, recursive, text, limit, keywords)

tag:指定標籤
    bs4Object.findAll("div")
    
attributes:屬性{}
    bs4Object.findAll("div", {"id", "content"})
    bs4Object.findAll("div", {"id", {"content", "content2"}})
    
recursive:遞歸 (True = 一路走訪標籤的子代, False = 只找最上層標籤)
    bs4Object.findAll("div", recursive = True)
    
text:文字比對
    print(len(bs4Object.findAll(text = "content")))
    7

limit:???

keywords:關鍵字 (選取包含特定屬性的標籤)
    bs4Object.findAll(id = "content")
    bs4Object.findAll("", {"id", "content"})
"""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""
處理晚輩:
    
bs4Object.findAll("div", {"id", "content"}).children
    呼叫子代標籤
    
bs4Object.findAll("div", {"id", "content"}).descendants
    呼叫兩打子孫標籤
"""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""
處理平輩:

bs4Object.findAll("div", {"id", "content"}).next_siblings
    呼叫自己(不包含)以下的同級標籤(多個)
bs4Object.findAll("div", {"id", "content"}).next_sibling
    呼叫自己(不包含)以下的同級標籤(1個)
    
bs4Object.findAll("div", {"id", "content"}).previous_siblings
    呼叫自己(不包含)以上的同級標籤(多個)
bs4Object.findAll("div", {"id", "content"}).previous_sibling
    呼叫自己(不包含)以上的同級標籤(1個)
"""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""
處理長輩:

bs4Object.findAll("div", {"id", "content"}).parent
    呼叫自己最近的一個親代標籤
    
bs4Object.findAll("div", {"id", "content"}).parents
    呼叫祖宗18代, 把太奏從墳墓裡面挖出來
"""""""""""""""""""""""""""""""""""""""""""""""""""""
