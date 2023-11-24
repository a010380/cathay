from selenium.webdriver.common.by import By
from .milelens_login_page import MilelensLoginPage
from Test_framework.utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH  # 引入配置
import csv
import datetime
from ..common.page import Page
from time import sleep
from utils.assertion import *
from selenium.webdriver.common.keys import Keys
from utils.log import logger

# milelens網紅搜尋、AI智慧搜尋、網紅熱門排行、網紅收藏庫

class MilelensHotTopic(MilelensLoginPage):
    excel = DATA_PATH + '/milelens_ai_search.xlsx'

    # 熱門話題
    close_popup = (By.XPATH, '//*[@data-test-id="welcomeModalDoNotRemind"]')  #popup的不要再提醒我        (By.XPATH, '')  #
    go_to_kol_search = (By.XPATH, '//*[@id="__next"]/div[1]/header/div/div/a[3]')  #上方列表的 熱門話題
    top1 = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]')  #熱門話題排行top1
    top2 = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[1]/div/div[2]')  #熱門話題排行top2
    top3 = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[1]/div/div[3]')  #熱門話題排行top3
    top4 = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[1]/div/div[4]')  #熱門話題排行top4
    top5 = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[1]/div/div[5]')  #熱門話題排行top5
    see_more = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[2]/div[3]/button')  #查看更多
    tag_topic_name = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/h2')  #熱門話題名稱
    # 網紅熱門排行
    s = (By.XPATH, '')  #
    s = (By.XPATH, '')  #
    s = (By.XPATH, '')  #
    s = (By.XPATH, '')  #
    s = (By.XPATH, '')  #
    s = (By.XPATH, '')  #
    s = (By.XPATH, '')  #
    s = (By.XPATH, '')  #
    s = (By.XPATH, '')  #
    s = (By.XPATH, '')  #
    s = (By.XPATH, '')  #
    s = (By.XPATH, '')  #
    

    # 熱門話題排行 將第一到第五中的所有貼文點進去檢查是否有關鍵字
    def hotTopicRank(self):
        # 過度時期
        self.find_element(*self.close_popup).click()
        self.find_element(*self.close_popup).click()
        self.wait()
        self.find_element(*self.top1).click()
        self.scroll_script("500")
        self.find_element(*self.see_more).click()
        self.scroll_script("300")
        self.wait()
        self.goThrough()
        self.find_element(*self.top2).click()
        self.scroll_script("500")
        self.find_element(*self.see_more).click()
        self.scroll_script("300")
        self.wait()
        self.goThrough()
        self.find_element(*self.top3).click()
        self.scroll_script("500")
        self.find_element(*self.see_more).click()
        self.scroll_script("300")
        self.wait()
        self.goThrough()
        self.find_element(*self.top4).click()
        self.scroll_script("500")
        self.find_element(*self.see_more).click()
        self.scroll_script("300")
        self.wait()
        self.goThrough()
        self.find_element(*self.top5).click()
        self.scroll_script("500")
        self.find_element(*self.see_more).click()
        self.scroll_script("300")
        self.wait()
        self.goThrough()
    
    # 熱門話題排行 將第一到第五中的所有貼文點進去檢查是否有關鍵字
    def kolHotRank(self):
        self.find_element(*self.close_popup).click()
        self.find_element(*self.close_popup).click()
        self.wait()
        self.scroll_script("1200")
        # 創建一個 CSV 檔案，如果檔案不存在則建立，如果已存在則附加資料
        with open("data.csv", "a", newline="") as csvfile:
            # 定義 CSV 欄位名稱
            fieldnames = ["Date", "fb_1_1", "fb_1_2", "fb_1_3", "fb_1_4", "fb_1_5", "fb_2_1", "fb_2_2", "fb_2_3", "fb_2_4", "fb_2_5", "fb_3_1", "fb_3_2", "fb_3_3", "fb_3_4", "fb_3_5", "fb_4_1", "fb_4_2", "fb_4_3", "fb_4_4", "fb_4_5", "fb_5_1", "fb_5_2", "fb_5_3", "fb_5_4", "fb_5_5"
                            , "ig_1_1", "ig_1_2", "ig_1_3", "ig_1_4", "ig_1_5", "ig_2_1", "ig_2_2", "ig_2_3", "ig_2_4", "ig_2_5", "ig_3_1", "ig_3_2", "ig_3_3", "ig_3_4", "ig_3_5", "ig_4_1", "ig_4_2", "ig_4_3", "ig_4_4", "ig_4_5", "ig_5_1", "ig_5_2", "ig_5_3", "ig_5_4", "ig_5_5"
                            , "yt_1_1", "yt_1_2", "yt_1_3", "yt_1_4", "yt_1_5", "yt_2_1", "yt_2_2", "yt_2_3", "yt_2_4", "yt_2_5", "yt_3_1", "yt_3_2", "yt_3_3", "yt_3_4", "yt_3_5", "yt_4_1", "yt_4_2", "yt_4_3", "yt_4_4", "yt_4_5", "yt_5_1", "yt_5_2", "yt_5_3", "yt_5_4", "yt_5_5"]
            # 建立 CSV 寫入器
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # 如果檔案是新建的，則寫入標題行
            if csvfile.tell() == 0:
                writer.writeheader()
            list=[]
            for g in range(1, 4):
                for i in range(1, 7):
                    self.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[3]/div[2]/div[' + str(g) + ']/div/div/div[3]/div[' + str(i) + ']/span').click()
                    self.implicitly_wait()
                    try:
                        for j in range(1, 6):
                            kol_name = self.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[3]/div[2]/div[' + str(g) + ']/div/div/div[4]/div[' + str(j) + ']//div/h6').text
                            print(kol_name)
                            self.implicitly_wait()
                            list.append(kol_name)
                    except:
                        list.append('空值')
            
            print(list)

    def test(self):
        # 過度時期
        self.wait()
        self.find_element(*self.close_popup).click()
        self.find_element(*self.close_popup).click()
        self.wait()
        today = datetime.date.today()
        print(today)

    # 將熱門話題底下的文章全部點過一次
    def goThrough(self):
        for i in range(1, 13):
            topic_name = self.find_element(*self.tag_topic_name).text
            topic_name = topic_name.replace('# ', '')
            try:
                self.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[2]/div[3]/div/div[' + str(i) + ']/div/div[1]').click()
                self.switch_to_window()
                self.wait()
                int_topic_name = self.check_page_source(topic_name)
                print('第' + str(i) + '篇的' + topic_name + '關鍵字數量為：' + str(int_topic_name))
                self.close()
                self.wait()
                self.switch_to_window()
            except:
                logger.warning('這個關鍵字的文章只到第' + str(i) + '篇')
        self.scroll_script("-800")
        self.wait()