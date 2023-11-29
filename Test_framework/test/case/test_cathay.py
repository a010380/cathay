import sys, os
# print(sys.path)
sys.path.append(os.getcwd())
import time
import unittest  # 单元测试模块
from Test_framework.utils.config import Config  # 引入配置
from Test_framework.test.page.cathay_login_page import CathayLoginPage
from selenium.common.exceptions import TimeoutException

class TestMilelens_3(unittest.TestCase):
    URL = Config().get('cathay')
    

    def sub_setUp(self):
        try:
            self.page = CathayLoginPage(browser_type='chrome').get(self.URL, maximize_window=True)
        except TimeoutException:
            print("Page load timed out. Retrying...")

    def test_search(self):
        self.sub_setUp()
        time.sleep(1)
        self.page.login()
        


        

if __name__ == '__main__':
    unittest.main()
    
    