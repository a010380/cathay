import time
import os
from selenium import webdriver
from utils.config import DRIVER_PATH, REPORT_PATH
from wqrfnium.wqrfnium import *
#新增的，相對應35~38行
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome

# 根据传入的参数选择浏览器的driver去打开对应的浏览器

# 可根据需要自行扩展
CHROMEDRIVER_PATH = DRIVER_PATH + '/chromedriver'
IEDRIVER_PATH = DRIVER_PATH + '/IEDriverServer.exe'
# PHANTOMJSDRIVER_PATH = DRIVER_PATH + '\phantomjs.exe'

TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Ie}
EXECUTABLE_PATH = {'firefox': 'wires', 'chrome': CHROMEDRIVER_PATH, 'ie': IEDRIVER_PATH}


class UnSupportBrowserTypeError(Exception):
    pass


class Browser(object):
    def __init__(self, browser_type='chrome'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s!' % ', '.join(TYPES.keys()))
        self.driver = None

    def get(self, url, maximize_window=True, implicitly_wait=30):
        print('CHROMEDRIVER_PATH的路徑為：' + CHROMEDRIVER_PATH)
        # 建立一個 Service 物件，並指定瀏覽器驅動程式的路徑
        service = Service(executable_path=EXECUTABLE_PATH[self._type])
        # 使用 Service 物件建立 Chrome 瀏覽器的 WebDriver
        self.driver = Chrome(service=service)
        
        # self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        # self.driver = self.browser(executable_path="/Users/xiaozhongwai/Desktop/Test-master/Test_framework/drivers/chromedriver")
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self

    def save_screen_shot(self, name='screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = REPORT_PATH + '\screenshot_%s' % day
        print('screenshot_path: ' + screenshot_path)
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
        print(screenshot_path + '\\%s_%s.png' % (name, tm))
        return screenshot

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

# 这里试验了一下保存截图的方法，保存png截图到report目录下。
if __name__ == '__main__':
    begin_wqrf(r'MyElements.xls')
    b = Browser('chrome').get('https://milelens.com/')
    b.save_screen_shot('test_baidu')
    time.sleep(3)
    b.quit()
