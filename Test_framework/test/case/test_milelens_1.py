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
from Test_framework.test.page.milelens_audience_mgmt import MilelensAudienceManagementPage


#本頁(受眾管理)已遭到棄用QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
class TestMilelens_1(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/milelens.xlsx'

    def sub_setUp(self):
        # 初始页面是Milelens Login page，传入浏览器类型打开浏览器
        self.page = MilelensLoginPage(browser_type='chrome').get(self.URL, maximize_window=True)

    def sub_tearDown(self):
        pass

    def test_search(self):
        datas = ExcelReader(self.excel).data
        # for d in datas:
        #     with self.subTest(data=d):
        self.sub_setUp()
        self.page.login('kson02@mailnesia.com', 'Pass1234')   #回推到22行 self.page = MilelensLoginPage(browser_type='chrome').get(self.URL, maximize_window=True)
        time.sleep(1)

        print('新增tag')
        self.page = MilelensAudienceManagementPage(self.page)
        self.page.addNewTag()
        self.page.add_tag_to_one()
        self.page.delete_tag()




if __name__ == '__main__':
    unittest.main()
