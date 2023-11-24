from selenium.webdriver.common.by import By
from .milelens_login_page import MilelensLoginPage
from ..common.page import Page
from time import sleep
from utils.assertion import assertNormalError, assertVariableError

# milelens首頁與封装的Milelens彈出視窗

class MilelensMainPage(MilelensLoginPage):
    milelens_logo = (By.XPATH, '//*[@data-test-id="logo"]')  #milelens的Logo
    close_popup = (By.XPATH, '//*[@id=":rk:"]/button/svg')  #popup的關閉        (By.XPATH, '')  #popup的
    no_notified_again = (By.XPATH, '//*[@data-test-id="welcomeModalDoNotRemind"]')  #popup的不要再提醒我
    go_to_main_page = (By.XPATH, '//*[@data-test-id="welcomeModalGoToHomePageButton"]')  #popup的前往首頁
    go_to_product_analysis = (By.XPATH, '//*[@data-test-id="welcomeModalGoToCompetitorButton"]')  #popup的競品分析
    go_to_product_monitor = (By.XPATH, '//*[@data-test-id="welcomeModalGoToCompetitorMonitorButton"]')  #popup的競品監測
    # go_to_member_mgmt = (By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div[4]/button')  #popup的受眾管理
    product_compare = (By.XPATH, '//*[@data-test-id="homePageCompetitorButton"]')  #競品比較
    my_fanpage = (By.XPATH, '//*[@data-test-id="homePageInsightButton"]')  #我的粉專
    mui_svg_icon = (By.XPATH, '//*[@data-test-id="homePageInsightPostTableExpander-0"]')  #粉專的貼文第一篇的摺疊

    def popup(self):
        self.wait()
        self.find_element(*self.go_to_main_page).click()
        self.refresh()
        self.wait()
        self.find_element(*self.go_to_product_analysis).click()
        self.wait()
        self.back()
        self.wait()
        self.find_element(*self.go_to_product_monitor).click()
        self.wait()
        self.back()
        self.wait()
        self.find_element(*self.no_notified_again).click()  # 尋找登入按鈕後點擊按鈕

    def checkFanPageList(self, keywords):
        try:
            self.find_element(*self.milelens_logo).click()
        except:
            pass
        self.wait()
        self.find_element(*self.close_popup).click()
        for i in range(2,7):
            fanpage_name = self.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div['+ str(i) +']/span').text
            print(fanpage_name)
            if fanpage_name in keywords:
                continue
            else:
                assertNormalError()
        print('done!!!!')

    def myFanPageCheckFanpagePostPic(self):
        # self.find_element(*self.milelens_logo).click()
        # self.implicitly_wait()
        # self.find_element(*self.close_popup).click()
        # self.implicitly_wait()
        self.find_element(*self.my_fanpage).click()
        self.wait()
        print('向下滑動750個像素')
        js = "window.scrollBy(0,750)"  # 向下滑動500個像素
        self.execute_script(js)
        self.wait()
        print('把第一篇文章的圖表展開收回去')
        self.find_element(*self.mui_svg_icon).click()
        for i in range(1, 16):
            flag=True
            try:
                self.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div[2]/div/div[5]/div/div[2]/div/div[1]/table/tbody/tr['+ str(i) +']/td[2]/div/div[1]/span/img')
                print('第'+ str(i) +'個沒問題')
                self.implicitly_wait()
            except:
                flag=False
                print('第'+ str(i) +'個沒顯示圖片！！！！')
                # assertVariableError(flag)