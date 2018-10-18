#from selenium import webdriver
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.ui import WebDriverWait
from urllib.request import urlopen
from urllib.error import URLError
import pymysql
import json
import time


#driver = webdriver.Chrome("C:\selenium_driver_chrome\chromedriver.exe")

thisyear = int(time.strftime('%Y', time.localtime(time.time())))


while True:

    enter = int(input("輸入公司股票代號: "))
    start_time = time.time()
    break

def get_data(year = thisyear, enter = enter):
    try:
        with urlopen("http://www.twse.com.tw/exchangeReport/STOCK_DAY_AVG?response=json&date="+str(year)+"0101&stockNo="+str(enter)) as url:
            data = json.loads(url.read().decode())   
    except URLError:
        print('URL error')
    else:
        return data


def get_title(year = 0):
    data = get_data(year)
    dict_stock = data.get("title")
    return dict_stock


def get_price(year = 0):
    data = get_data(year)
    dict_data = data.get("data")
    list_data = dict_data[0][1]
    return list_data


def get_result():
    for year in range(thisyear, thisyear-10, -1):
        print(get_title(year))
        time.sleep(1)
        print(get_price(year))
        time.sleep(1)
    end_time = time.time()
    print("總共花費"+str(end_time-start_time)+"秒鐘")
get_result()
        
