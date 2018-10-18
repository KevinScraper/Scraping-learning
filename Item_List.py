from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import re


chrome_options = Options()
chrome_options.add_argument("--headless")  #新增driver參數"--headless", 瀏覽器隱藏狀態開啟
#(driver下載: https://sites.google.com/a/chromium.org/chromedriver/downloads)
driver = webdriver.Chrome("C:\selenium_driver_chrome\chromedriver.exe", chrome_options = chrome_options)
driver.get("http://isin.twse.com.tw/isin/C_public.jsp?strMode=2")

html = driver.page_source
bs4Object = BeautifulSoup(html, "lxml")
listed_company_len = len(bs4Object.find_all(text="ESVUFR"))  #上市公司數量
content_list = []

"""""
從台灣證劵交易所抓取所有最新上市公司代碼
"""""
def company_item_list():
    filtrate = re.compile(u'[^0-9]')
    for i in range(2, listed_company_len + 3):
        filter_result = filtrate.sub(r'', bs4Object.find_all("tr")[i].td.get_text())
        content_list.append(filter_result)
        
    driver.quit()
    return content_list

