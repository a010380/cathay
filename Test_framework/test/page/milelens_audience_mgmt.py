from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .milelens_login_page import MilelensLoginPage
from Test_framework.utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH  # 引入配置
from utils.file_reader import ExcelReader  # 引入xls读取模块
from ..common.page import Page
from time import sleep
import xlrd
import datetime
from utils.assertion import assertNormalError

# 封装的Milelens受眾管理頁

class MilelensAudienceManagementPage(MilelensLoginPage):
    excel = DATA_PATH + '/milelens_search_items.xlsx'

    #受眾管理的元素們                                    (By.XPATH, '')  #
    close_popup = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/button[1]')  #popup的關閉
    audience_mgmt = (By.XPATH, '//*[@id="__next"]/div[1]/header/div/div/a[3]/h6')  #受眾管理頁
    recent_added_tags = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/span')  #最近新增的tag
    add_new_tag = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div[2]/div/div[3]/button')  #建立新標籤按鈕
    tag_name_input = (By.XPATH, '/html/body/div[3]/div[3]/div/div/form/div/div/div[2]/input')  #輸入匡
    create_tag = (By.XPATH, '/html/body/div[3]/div[3]/div/div/form/div/button')  #建立tag按鈕
    close_create_tag_popup = (By.XPATH, '/html/body/div[3]/div[3]/div/h2/div/button')  #建立新標籤的關閉鈕

    second_user_checkbox = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div[2]/div/div[5]/div/div[1]/table/tbody/tr[2]/td[1]/span/input')  #第二個用戶的checkbox
    attach_tag = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div[2]/div/div[4]/div[2]/div[1]/div/button')  #貼上標籤
    attach_tag_attach_tag = (By.XPATH, '/html/body/div[3]/div/div/ul/div/li[1]')  #貼上標籤第二層：貼上標籤
    attach_tag_attach_blacklist_tag = (By.XPATH, '/html/body/div[3]/div/div/ul/div/li[2]')  #貼上標籤第二層：貼上黑名單標籤
    detach_tag = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div[2]/div/div[4]/div[2]/div[2]/div/button')  #撕下標籤
    detach_tag_detach_tag = (By.XPATH, '/html/body/div[3]/div/div/ul/div/li[1]')  #撕下標籤第二層：撕下標籤
    detach_tag_detach_blacklist_tag = (By.XPATH, '/html/body/div[3]/div/div/ul/div/li[2]')  #撕下標籤第二層：撕下黑名單標籤
    tag_pool_no1 = (By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div/ul/li[1]')  #批次貼上標籤中的第一個標籤
    tag_pool_no1_tag = (By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div/ul/li[1]/div/span')  #批次貼上標籤中的第一個標籤(點擊用)
    attach_button = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/button[2]')  #貼上按鈕
    attach_tag_success_toast = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[1]/div/div/div[2]')  #貼上成功的toast
    second_user_recent_tag = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div[2]/div/div[5]/div/div[1]/table/tbody/tr[2]/td[6]/div/div[1]/span')  #第二個用戶的最近一筆tag
    first_user_black_block = (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[5]/div/div[1]/table/tbody/tr[1]/td[7]')  #第一筆用戶的黑名單區塊
    first_user_edit = (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[5]/div/div[1]/table/tbody/tr[1]/td[8]/div/div/button')  #第一筆用戶的編輯
    user_edit_edit_tag = (By.XPATH, '/html/body/div[3]/div/div/ul/div/li[1]')  #用戶編輯的編輯標籤
    user_edit_edit_blacklist_tag = (By.XPATH, '/html/body/div[3]/div/div/ul/div/li[2]')  #用戶編輯的編輯黑名單標籤
    edit_tag_no1 = (By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div/ul/li[1]')  #編輯標籤中的第一個標籤
    first_user_recent_tag = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div[2]/div/div[5]/div/div[1]/table/tbody/tr[2]/td[6]/div/div[1]/span')  #第一個用戶的最近一筆tag
    save_button = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/button[2]')  #儲存按鈕
    edit_tag_success_toast = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[1]/div/div/div[2]')  #編輯成功的toast
    search_tags_pool = (By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div[1]/div/div/div/div[1]')  #

    #建立新的標籤
    def addNewTag(self):
        self.find_element(*self.close_popup).click()
        self.find_element(*self.audience_mgmt).click()
        recentNewTag = self.find_element(*self.recent_added_tags).text
        print('最近新增的tag: ' + recentNewTag)
        
        today = datetime.date.today()
        month = today.month
        day = today.day
        tagName = '{:0>2d}'.format(month) + '{:0>2d}'.format(day)
        print('預計要新增的tag: ' + tagName)
        if tagName == recentNewTag:
            print('今天已經建立過tag了')
        else:
            print('執行新增tag流程')
            self.find_element(*self.add_new_tag).click()
            self.implicitly_wait()
            self.find_element(*self.tag_name_input).click()
            self.find_element(*self.tag_name_input).clear()
            self.wait()
            self.find_element(*self.tag_name_input).send_keys(tagName)
            self.find_element(*self.create_tag).click()
            self.wait()
            self.find_element(*self.close_create_tag_popup).click()
            recentNewTag = self.find_element(*self.recent_added_tags).text
            print('tagName: ' + tagName + ', recentNewTag: ' + recentNewTag)
            if tagName == recentNewTag:
                print('建立成功！！')
                
            else:
                assertNormalError()

    #以勾選用戶的方式，點擊貼上標籤的方式去貼上tag
    def add_tag_to_one(self):
        self.refresh()
        self.find_element(*self.audience_mgmt).click()
        self.implicitly_wait()
        #先在第二筆用戶用點擊編輯的方式新增標籤
        self.find_element(*self.second_user_checkbox).click()
        self.find_element(*self.attach_tag).click()
        self.implicitly_wait()
        self.find_element(*self.attach_tag_attach_tag).click()
        self.wait()
        
        aria_selected1 = self.find_element(*self.tag_pool_no1).get_attribute("aria-selected")
        if aria_selected1 == 'false':
            self.find_element(*self.tag_pool_no1).click()
        else:
            print('最新建立的tag已經貼上該用戶')
        self.find_element(*self.attach_button).click()
        self.implicitly_wait()
        #兩種方式檢查新增是否成功
        try:
            self.find_element(*self.attach_tag_success_toast)
        except:
            print('沒有toast')
            assertNormalError()
        try:
            secondUserTag = self.find_element(*self.second_user_recent_tag).text
            recentNewTag = self.find_element(*self.recent_added_tags).text
            secondUserTag == recentNewTag
        except:
            print('tag對照不一致')
            assertNormalError()

        #在第一筆用戶勾選並貼上標籤，直接將鼠標移到用戶列表最右邊的編輯去貼上tag
        self.wait()
        self.wait()
        self.find_element(*self.first_user_black_block).click()
        self.find_element(*self.first_user_edit).click()
        self.implicitly_wait()
        self.find_element(*self.user_edit_edit_tag).click()
        self.implicitly_wait()
        aria_selected2 = self.find_element(*self.edit_tag_no1).get_attribute("aria-selected")
        if aria_selected2 == 'false':
            self.find_element(*self.edit_tag_no1).click()
        else:
            print('最新建立的tag已經貼上該用戶')
        self.find_element(*self.save_button).click()
        self.wait()
        self.save_screen_shot()
        
        try:
            self.find_element(*self.edit_tag_success_toast)
        except:
            print('沒有toast')
            assertNormalError()
        self.wait()
        self.wait()
        try:
            firstUserTag = self.find_element(*self.first_user_recent_tag).text
            recentNewTag = self.find_element(*self.recent_added_tags).text
            firstUserTag == recentNewTag
        except:
            print('tag對照不一致')
            assertNormalError()

    def delete_tag(self):
        self.refresh()
        #單獨測試刪除功能需要加入!!!!!!!!!!!!!
        # self.find_element(*self.close_popup).click()
        #單獨測試刪除功能需要加入!!!!!!!!!!!!!
        self.find_element(*self.audience_mgmt).click()
        self.implicitly_wait()
        recentNewTag = self.find_element(*self.recent_added_tags).text

        #先從第一個會員的tag開始處理
        try:
            self.find_element(*self.first_user_recent_tag)
            self.find_element(*self.first_user_black_block).click()
            self.find_element(*self.first_user_edit).click()
            self.implicitly_wait()
            self.find_element(*self.user_edit_edit_tag).click()
            #這邊如果有兩個tag以上存在的話，元素的xpath會變成/html/body/div[3]/div[3]/div/div[1]/div/div[1]/div/div/div/div[1]/div/svg
            # for i in range(1, 10):
            if self.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div[1]/div/div/div/div'):
                tag_name = self.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div[1]/div/div/div/div').text
                if tag_name == recentNewTag:
                    print('進入到點擊環節')
                    self.find_element(*self.edit_tag_no1).click()
                    self.wait()
                    self.find_element(*self.save_button).click()
                    self.wait()
        except:
            print('這個會員目前沒有tag')
        
        #處理第二個會員以勾選、撕下標籤的方式
        self.find_element(*self.second_user_checkbox).click()
        self.find_element(*self.detach_tag).click()
        self.implicitly_wait()
        self.find_element(*self.detach_tag_detach_tag).click()
        aria_selected1 = self.find_element(*self.tag_pool_no1).get_attribute("aria-selected")
        if aria_selected1 == 'false':
            self.find_element(*self.tag_pool_no1).click()
        else:
            print('最新建立的tag已經貼上該用戶')
        self.find_element(*self.attach_button).click()
        self.wait()