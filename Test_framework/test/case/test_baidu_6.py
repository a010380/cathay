import os
import time
import unittest  # 单元测试模块
from selenium import webdriver  # 引入浏览器驱动
from selenium.webdriver.common.by import By  # 引入xpath查找模块
from utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH  # 引入配置
from utils.log import logger # 引入日志模块
from utils.file_reader import ExcelReader  # 引入xls读取模块
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email
from test.page.milelens_result_page import MilelensLoginPage, MilelensResultPage

class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/milelens.xlsx'

    def sub_setUp(self):
        # 初始页面是Milelens Login page，传入浏览器类型打开浏览器
        self.page = MilelensLoginPage(browser_type='chrome').get(self.URL, maximize_window=True)

    def sub_tearDown(self):
        pass

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.login('kson01@mailnesia.com', 'Pass1234')   #回推到19行 self.page = MilelensLoginPage(browser_type='chrome').get(self.URL, maximize_window=True)
                time.sleep(2)


                self.page = MilelensResultPage(self.page)  # 页面跳转到result page
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()

if __name__ == '__main__':
    unittest.main()

    report = REPORT_PATH + '\\report.html'
    print(report)
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='克森全站', description='修改html報告')
        runner.run(TestBaiDu('test_search'))

    # e = Email(title='百度搜索测试报告',
    #           message='这是今天的测试报告，请查收！',
    #           receiver='...',
    #           server='...',
    #           sender='...',
    #           password='...',
    #           path=report
    #           )
    # e.send()