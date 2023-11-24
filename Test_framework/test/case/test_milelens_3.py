import sys, os, logging
# print(sys.path)
sys.path.append(os.getcwd())
import time
import unittest  # 单元测试模块
from selenium import webdriver  # 引入浏览器驱动
from selenium.webdriver.common.by import By  # 引入xpath查找模块
from Test_framework.utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH  # 引入配置
from utils.log import logger # 引入日志模块
from utils.file_reader import ExcelReader  # 引入xls读取模块
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email
from utils.assertion import assertHTTPCode
from Test_framework.test.page.milelens_result_page import MilelensLoginPage, MilelensResultPage
from Test_framework.test.page.milelens_main_page import MilelensMainPage
from Test_framework.test.page.milelens_product_analysis_page import MilelensProductAnalysisPage
from Test_framework.test.page.milelens_kol_search import MilelensKolSearch

class TestMilelens_3(unittest.TestCase):
    URL = Config().get('staging_URL')
    excel = DATA_PATH + '/milelens.xlsx'

    def sub_setUp(self):
        # 初始页面是Milelens Login page，传入浏览器类型打开浏览器
        self.page = MilelensLoginPage(browser_type='chrome').get(self.URL, maximize_window=True)

    def test_search(self):
        self.sub_setUp()
        self.page.login('kson06@mailnesia.com', 'Qaz2wsx3edc')   #回推到22行 self.page = MilelensLoginPage(browser_type='chrome').get(self.URL, maximize_window=True)
        time.sleep(1)

        
        self.page = MilelensKolSearch(self.page)
        # print('網紅搜尋 搜尋一個關鍵字 在該網紅中檢查4個tab有沒有資料')
        # self.page.kolSearchAndCheckData()
        # print('AI智慧搜尋 根據excel表的關鍵字輸入並搜尋 得到的結果檢查是否合乎邏輯')
        # self.page.aiSearch()
        # print('網紅熱門排行 先選擇平台 在選擇粉絲數 最後切換tab')
        # self.page.kolHotRank()
        self.page.postKeywords()
        


        

if __name__ == '__main__':
    unittest.main()

    # e = Email(title='百度搜索测试报告',
    #           message='这是今天的测试报告，请查收！',
    #           receiver='...',
    #           server='...',
    #           sender='...',
    #           password='...',
    #           path=report
    #           )
    # e.send()