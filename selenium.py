from selenium import webdriver

#指定ChromeDriver路徑(driver下載: https://sites.google.com/a/chromium.org/chromedriver/downloads)
driver = webdriver.Chrome("C:\selenium_driver_chrome\chromedriver.exe")

#開啟&取得指定頁面
driver.get("https://m.sportslottery.com.tw/zh/home")

#用Xpath找尋指定的屬性元素 然後輸入文字
#driver.find_element_by_xpath("//input[@id='lst-ib']").send_keys("天氣")

#用Xpath找尋指定的屬性元素 然後點擊
#driver.find_element_by_xpath("//input[@jsaction='sf.chk']").submit()
