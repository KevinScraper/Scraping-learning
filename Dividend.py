from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import pymysql
import time
import re

import Item_list


"""""
從Item_list拿取所有上市編號
"""""
while True:
    enter = Item_list.company_item_list()
    break


"""""
開啟瀏覽器到"股利政策"頁面
"""""
"""(隱藏瀏覽器用這串)
chrome_options = Options()
chrome_options.add_argument("--headless")  #新增driver參數"--headless", 瀏覽器隱藏狀態開啟
#(driver下載: https://sites.google.com/a/chromium.org/chromedriver/downloads)
driver = webdriver.Chrome("C:\selenium_driver_chrome\chromedriver.exe", chrome_options = chrome_options)
"""
driver = webdriver.Chrome("C:\selenium_driver_chrome\chromedriver.exe")
try:
    driver.get("https://goodinfo.tw/StockInfo/index.asp")
except TimeoutException:
    print("Time out")
    driver.close()

#f = open("C:/Users/user/Desktop/testTest.txt", 'w', encoding = "utf-8")  #若無該txt檔則會自動新增

time.sleep(3)
element = driver.find_element_by_xpath('//*[@id="txtStockCode"]')
element.send_keys(enter[0])
time.sleep(1)
element.submit()
time.sleep(2)
inputelement = driver.find_element_by_xpath('//*[@id="StockDetailMenu"]/table/tbody/tr/td[1]/table/tbody/tr[12]/td/a')
inputelement.click()


"""""
解析瀏覽器網址
"""""

def analysisWebPage():
    html = driver.page_source  #page_source會抓取該網頁html
    #f.write("%s \n" %(html))  #抓取html寫入指定txt檔
    #f.close()
    return html


"""""
用beautifulsoup過濾需要的資料
"""""
def get_Every_Years_Dividend():
    list_content = []  #裝股利值的容器
    for stock_number in enter:
        element_2 = driver.find_element_by_xpath('//*[@id="txtStockCode"]')  #鎖定搜尋框
        element_2.send_keys(stock_number)  #在搜尋框輸入股票代碼
        time.sleep(1)
        element_2.submit()  #按下Enter
        bs4Object = BeautifulSoup(analysisWebPage(), "lxml")
        title = bs4Object.find_all("a",{"style":re.compile("^[font\-size]")})
        result = bs4Object.find_all("tr",{"onmouseover":re.compile("^[this]")})
        print("歷年現金股利(元/股):")
        print(title[3].get_text())
        for i in range(0, 10):  #抓取前10筆<tr onmouseover="this.style.background="#fff2cc";...>
            print('\n')
            for next in result[i].stripped_strings:
                list_content.append(next)  #將<tr onmouseover="this.style.background="#fff2cc";...>存入list
            if list_content[0] != "平均":
                print(list_content[0]+" "+list_content[3])
                del list_content[:]  #清空list
            else:
                del list_content[:]  #清空list
                break
        time.sleep(3)
    driver.quit()

get_Every_Years_Dividend()
