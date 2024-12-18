#載入selenium相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#設定chrome driver的執行檔路徑
options=Options() #建立Options的物件實體
options.chrome_executable_path=r'C:\Users\sandy\Desktop\python\python零基礎練習\chromedriver.exe'#chrome driver執行檔路徑
#建立driver物件實體，用程式操作瀏覽器運作
driver=webdriver.Chrome()#建立driver物件實體 #新的selenium 版本已經不要設定driver的路徑,系統會自動detect
driver.maximize_window()#視窗最大化
driver.get('https://www.google.com/')#放入想打開的網頁網址
driver.save_screenshot('screenshot-google.png')#做螢幕截圖
driver.get('https://www.ntu.edu.tw/')
driver.save_screenshot('screenshot-ntu.png')
driver.close()