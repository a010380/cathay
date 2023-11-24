from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .milelens_login_page import MilelensLoginPage
from Test_framework.utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH  # 引入配置
from utils.file_reader import ExcelReader  # 引入xls读取模块
from ..common.page import Page
from time import sleep
import xlrd

# 封装的Milelens競品分析頁

class MilelensProductAnalysisPage(MilelensLoginPage):
    excel = DATA_PATH + '/milelens_search_items.xlsx'

    #競品清單的元素們                                     (By.XPATH, '')  #
    product_analysis = (By.XPATH, '//*[@data-test-id="competitorPage"]')  #競品分析頁
    delete_product_list = (By.XPATH, '//*[@data-test-id="competitorPageDeleteCompetitorButton"]')  #刪除第一個競品
    hide_product_list = (By.XPATH, '//*[@data-test-id="competitorPageCompetitorVisibilityButton"]')  #隱藏第一個競品
    add_product = (By.XPATH, '//*[@data-test-id="competitorPageCompetitorButton"]')  #新增競品紐
    industry_list = (By.XPATH, '//*[@data-test-id="competitorModalIndustryButton"]')  #產業列表
    search_or_url= (By.XPATH, '//*[@data-test-id="competitorModalKeywordButton"]')  #搜尋或網址
    search_input_column= (By.XPATH, '//*[@data-test-id="competitorModalKeywordInput"]/input')  #輸入關鍵字欄位
    add_the_first_product = (By.XPATH, '//*[@data-test-id="competitorModalCompetitorTableAddButton-0"]')  #搜尋結果的第一個競品
    the_first_product_text = (By.XPATH, '//*[@data-test-id="competitorModalCompetitorTableItemName-0"]')  #搜尋結果的第一個競品名稱
    close_the_add_product_window = (By.XPATH, '//*[@data-test-id="competitorModalCloseButton"]')  #新增競品視窗的關閉鈕

    def deleteProductList(self):
        self.find_element(*self.product_analysis).click()
        self.implicitly_wait()
        for x in range(5):
            try:
                self.find_element(*self.delete_product_list).click()
                self.wait()
            except:
                pass

    def enterKeywordsAndAdd(self):
        datas = ExcelReader(self.excel).data
        print("Excel裡頭的關鍵字: ", datas)
        listKeywords = ['CloudMile 萬里雲']
        self.find_element(*self.product_analysis).click()
        self.wait()
        for d in datas:
            self.find_element(*self.add_product).click()
            self.find_element(*self.search_or_url).click()
            self.find_element(*self.search_input_column).click()
            self.find_element(*self.search_input_column).send_keys(d["關鍵字："])  # 尋找輸入匡後輸入excel表中的關鍵字
            self.wait()
            self.find_element(*self.add_the_first_product).click()
            keyword = self.find_element(*self.the_first_product_text).text
            listKeywords.append(keyword)
            print(listKeywords)
            self.wait()
            self.refresh()
        self.wait()
        return listKeywords
