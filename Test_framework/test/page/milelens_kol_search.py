import re
from selenium.webdriver.common.by import By
from .milelens_login_page import MilelensLoginPage
from Test_framework.utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH  # 引入配置
from utils.file_reader import ExcelReader  # 引入xls读取模块
from ..common.page import Page
from time import sleep
from utils.assertion import *
from selenium.webdriver.common.keys import Keys

# milelens網紅搜尋、AI智慧搜尋、網紅熱門排行、網紅收藏庫

class MilelensKolSearch(MilelensLoginPage):
    excel = DATA_PATH + '/milelens_ai_search.xlsx'
    excel1 = DATA_PATH + '/milelens_post_keywords.xlsx'

    # 網紅搜尋
    close_popup = (By.XPATH, '//*[@data-test-id="welcomeModalDoNotRemind"]')  #popup的不要再提醒我        (By.XPATH, '')  #
    go_to_kol_search = (By.XPATH, '//*[@id="__next"]/div[1]/header/div/div/a[4]')  #上方列表的 網紅搜尋
    kol_name_input = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[2]/div/div[1]/div[4]/div/div/div[2]/input')  #網紅名稱輸入欄
    search_button = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/button')  #網紅搜尋的搜尋按鈕
    click_first_kol = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[3]/h6')  #點擊第一個kol
    power_analysis = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[2]/button[1]/span') #聲量分析的按鈕
    facebook_analysis = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[2]/button[3]')  #facebook分析的按鈕
    instagram_analysis = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[2]/button[4]')  #instagram分析的按鈕
    youtube_analysis = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[2]/button[5]')  #youtube分析的按鈕
    # 聲量分析
    kol_power_analysis = (By.XPATH, '//*[@id="overview-volume-analysis"]/div/div[1]/div[1]/div/h4')  #網紅聲量分析
    kol_power_trend = (By.XPATH, '//*[@id="overview-volume-trend"]/div/div[1]/div[1]/div/h4')  #網紅聲量趨勢
    audience_analysis = (By.XPATH, '//*[@id="overview-audience-analysis"]/div/div[1]/div/div/h4')  #受眾分析
    comment_sentiment_analysis = (By.XPATH, '//*[@id="overview-comment-sentiment"]/div/div[1]/div[1]/div/h4')  #留言情緒分析
    overview_mentions = (By.XPATH, '//*[@id="overview-mentions"]/div/div[1]/div[1]/div/h4')  #正負面聲量
    # facebook分析
    fb_overall_power = (By.XPATH, '//*[@id="facebook-overview"]/div/div[1]/div[1]/div/h4')  #facebook整體成效
    fb_interactive_analysis = (By.XPATH, '//*[@id="facebook-interaction"]/div/div[1]/div[1]/div/h4')  #Facebook 互動分析
    fb_famous_interactive_topic = (By.XPATH, '//*[@id="facebook-hot-interaction"]/div/div[1]/div/div/h4')  #Facebook 熱門互動主題
    fb_discuss_analysis = (By.XPATH, '//*[@id="facebook-mention"]/div/div[1]/div/div/h4')  #Facebook 討論聲量分析
    fb_hashtag_analysis = (By.XPATH, '//*[@id="facebook-hashtag"]/div/div[1]/div[1]/div/h4')  #Facebook Hashtag 分析
    fb_views_analysis = (By.XPATH, '//*[@id="facebook-video-watch"]/div/div[1]/div[1]/div/h4')  #Facebook 觀看數分析
    fb_hot_post = (By.XPATH, '//*[@id="facebook-hot-post"]/div/div[1]/div[1]/div/h4')  #Facebook 熱門貼文
    # instagram分析
    ig_overall_power = (By.XPATH, '//*[@id="instagram-overview"]/div/div[1]/div[1]/div/h4')  #Instagram 整體成效
    ig_fans_trends = (By.XPATH, '//*[@id="instagram-fan-trend"]/div/div[1]/div/div/h4')  #Instagram 粉絲成長趨勢
    ig_interactive_analysis = (By.XPATH, '//*[@id="instagram-interaction"]/div/div[1]/div[1]/div/h4')  #Instagram 互動分析
    ig_views_analysis = (By.XPATH, '//*[@id="instagram-video-watch"]/div/div[1]/div[1]/div/h4')  #Instagram 觀看數分析
    ig_hot_interactive_topic = (By.XPATH, '//*[@id="instagram-popular-topic"]/div/div[1]/div/div/h4')  #Instagram 熱門互動主題
    ig_hot_posts = (By.XPATH, '//*[@id="instagram-popular-post"]/div/div[1]/div[1]/div/h4')  # Instagram 熱門貼文
    # Youtube分析
    yt_overview = (By.XPATH, '//*[@id="youtube-overview"]/div/div[1]/div[1]/div/h4')  #YouTube 整體成效
    yt_video_watch = (By.XPATH, '//*[@id="youtube-video-watch"]/div/div[1]/div[1]/div/h4')  #YouTube 觀看數分析
    yt_opoular_topic = (By.XPATH, '//*[@id="youtube-popular-topic"]/div/div[1]/div/div/h4')  #YouTube 熱門互動主題
    # ai智慧搜尋
    ai_smart_search = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[1]/button[2]')  #AI 智慧搜尋的tab             
    ai_smart_search_input = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div[2]/input')  #智慧搜尋輸入欄位
    ai_search_button = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/button')  #搜尋按鈕
    how_many_search_result = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[3]/div[1]/div[1]/div[1]/p')  #搜尋結果的筆數
    sort_by_button = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[3]/div[1]/div[1]/div[2]/div[1]/div')  #排序依
    sort_by_total_fans = (By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[3]')  #排序依總粉絲數
    first_kol_total_fans = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/h6')  #第一個kol的總粉絲數
    # 貼文關鍵字
    post_keyword = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[1]/button[3]')  #貼文關鍵字的tab
    post_keyword_input = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/input')  #貼文關鍵字輸入欄位
    post_keyword_button = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div[3]/button')  #貼文關鍵字搜尋
    # 網紅熱門排行
    kol_hot_rank = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[2]/div[1]/button[4]')  #網紅熱門排行的tab           (By.XPATH, '')  #
    family_tab = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/span')  #親子
    food_tab = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/span')  #美食
    pets_tab = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[3]/div[1]/div[2]/div[1]/div[3]/span')  #寵物
    finance_tab = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[3]/div[1]/div[2]/div[1]/div[4]/span')  #金融理財
    buy_together_tab = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[3]/div[1]/div[2]/div[1]/div[5]/span')  #團購開箱
    all_tab = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[3]/div[1]/div[2]/div[1]/div[6]/span')  #不分主題
    platform_button = (By.XPATH, '//*[@id="mui-component-select-platformId"]/div')  #平台下拉選單
    platform_button_fb = (By.XPATH, '//*[@id="menu-platformId"]/div[3]/ul/li[1]')  #平台fb
    platform_button_ig = (By.XPATH, '//*[@id="menu-platformId"]/div[3]/ul/li[2]')  #平台ig
    platform_button_yt = (By.XPATH, '//*[@id="menu-platformId"]/div[3]/ul/li[3]')  #平台ig
    fans_button = (By.XPATH, '//*[@id="mui-component-select-levelId"]')  #粉絲數下拉選單
    fans_button_1 = (By.XPATH, '//*[@id="menu-levelId"]/div[3]/ul/li[1]')  #不限
    fans_button_2 = (By.XPATH, '//*[@id="menu-levelId"]/div[3]/ul/li[2]')  #奈米網紅
    fans_button_3 = (By.XPATH, '//*[@id="menu-levelId"]/div[3]/ul/li[3]')  #微網紅
    fans_button_4 = (By.XPATH, '//*[@id="menu-levelId"]/div[3]/ul/li[4]')  #潛力網紅
    fans_button_5 = (By.XPATH, '//*[@id="menu-levelId"]/div[3]/ul/li[5]')  #中型網紅
    fans_button_6 = (By.XPATH, '//*[@id="menu-levelId"]/div[3]/ul/li[6]')  #中大型網紅
    fans_button_7 = (By.XPATH, '//*[@id="menu-levelId"]/div[3]/ul/li[7]')  #大型網紅
    fans_button_8 = (By.XPATH, '//*[@id="menu-levelId"]/div[3]/ul/li[8]')  #名人
    topic_rank_tbody = (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[3]/div[2]/div[1]/table/tbody')  #主題排行榜的tbody

    # 網紅搜尋，搜尋一個關鍵字，檢查4個tab有沒有資料
    def kolSearchAndCheckData(self):
        # 過度時期
        self.wait()
        self.find_element(*self.close_popup).click()
        self.find_element(*self.close_popup).click()
        self.wait()
        self.find_element(*self.go_to_kol_search).click()
        self.refresh()
        self.find_element(*self.kol_name_input).click()
        self.find_element(*self.kol_name_input).send_keys("joeman")
        self.wait()
        self.find_element(*self.search_button).click()
        self.wait()

        # 開始驗證聲量分析
        self.find_element(*self.click_first_kol).click()
        self.wait()
        self.switch_to_window()
        self.implicitly_wait()
        self.find_element(*self.power_analysis).click()
        self.wait()
        try:
            self.find_element(*self.kol_power_analysis)
            self.find_element(*self.kol_power_trend)
            self.find_element(*self.audience_analysis)
            self.find_element(*self.comment_sentiment_analysis)
            self.find_element(*self.overview_mentions)
            print('聲量分析passssssssssssssssssss')
        except:
            assertAnalysisError('聲量分析')
        self.find_element(*self.facebook_analysis).click()
        self.wait()
        try:
            self.find_element(*self.fb_overall_power)
            self.find_element(*self.fb_interactive_analysis)
            self.find_element(*self.fb_famous_interactive_topic)
            self.find_element(*self.fb_discuss_analysis)
            self.find_element(*self.fb_hashtag_analysis)
            self.find_element(*self.fb_views_analysis)
            self.find_element(*self.fb_hot_post)
            print('facebook分析passssssssssssssssssss')
        except:
            assertAnalysisError('facebook')
        self.find_element(*self.instagram_analysis).click()
        self.wait()
        try:
            self.find_element(*self.ig_overall_power)
            self.find_element(*self.ig_fans_trends)
            self.find_element(*self.ig_interactive_analysis)
            self.find_element(*self.ig_views_analysis)
            self.find_element(*self.ig_hot_interactive_topic)
            self.find_element(*self.ig_hot_posts)
            print('instagram分析passssssssssssssssssss')
        except:
            assertAnalysisError('instagram')
        self.find_element(*self.youtube_analysis).click()
        self.implicitly_wait()
        try:
            self.find_element(*self.yt_overview)
            self.find_element(*self.yt_video_watch)
            self.find_element(*self.yt_opoular_topic)
            print('youtube分析passssssssssssssssssss')
        except:
            assertAnalysisError('youtube')
        self.close()
        self.wait()
        self.switch_to_window()

    # AI智慧搜尋，根據excel表的關鍵字輸入並搜尋，得到的結果檢查是否合乎邏輯
    def aiSearch(self):
        try:
            self.find_element(*self.close_popup).click()
        except:
            pass
        self.find_element(*self.go_to_kol_search).click()
        self.find_element(*self.go_to_kol_search).click()
        self.implicitly_wait()
        self.find_element(*self.ai_smart_search).click()
        datas = ExcelReader(self.excel).data
        print("AI搜尋中   Excel裡頭的關鍵字: ", datas)
        for d in datas:
            self.find_element(*self.ai_smart_search_input).click()
            self.wait()
            # self.find_element(*self.ai_smart_search_input).clear()
            self.find_element(*self.ai_smart_search_input).send_keys(Keys.COMMAND + 'a')
            self.find_element(*self.ai_smart_search_input).send_keys(Keys.DELETE)
            self.implicitly_wait()
            self.find_element(*self.ai_smart_search_input).click()
            self.find_element(*self.ai_smart_search_input).send_keys(d["關鍵字："])  # 尋找輸入匡後輸入excel表中的關鍵字
            self.wait()
            self.find_element(*self.ai_search_button).click()
            self.wait()
            result_amount = self.find_element(*self.how_many_search_result).text
            new_result_amount = result_amount.replace(" 位網紅", "")
            int_result_amount = int(new_result_amount)
            print(int_result_amount)
            if int_result_amount == 0:
                assertNormalError()
            # 這邊開始做排序並檢查資料是否正確
            self.find_element(*self.sort_by_button).click()
            self.implicitly_wait()
            self.find_element(*self.sort_by_total_fans).click()
            self.wait()
            first_kol_total_fans = self.find_element(*self.first_kol_total_fans).text
            if ',' in first_kol_total_fans:
                first_kol_total_fans = first_kol_total_fans.replace(',', '')
            kol_total_fans = int(first_kol_total_fans)
            previous_total_fans = kol_total_fans
            for i in range(3, 5):
                total_fans = self.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[3]/div[' + str(i) + ']/div/div[2]/div[2]/div/div[2]/div/div[2]/h6').text
                if ',' in total_fans:
                    total_fans = total_fans.replace(',', '')
                int_total_fans = int(total_fans)
                if previous_total_fans > int_total_fans:
                    previous_total_fans = int_total_fans
                else:
                    assertNormalError()
    
    # 貼文關鍵字，輸入各種AND/OR的排列組合去檢查答案是否正確
    def postKeywords(self):
        self.find_element(*self.close_popup).click()
        self.find_element(*self.close_popup).click()
        self.find_element(*self.go_to_kol_search).click()
        self.implicitly_wait()
        self.find_element(*self.post_keyword).click()
        self.find_element(*self.post_keyword_input).click()
        datas = ExcelReader(self.excel1).data
        print("貼文關鍵字中  Excel裡頭的關鍵字: ", datas)
        for d in datas:
            self.find_element(*self.post_keyword_input).click()
            self.implicitly_wait()
            self.find_element(*self.post_keyword_input).send_keys(Keys.COMMAND + 'a')
            self.find_element(*self.post_keyword_input).send_keys(Keys.DELETE)
            self.implicitly_wait()
            self.find_element(*self.post_keyword_input).click()
            self.find_element(*self.post_keyword_input).send_keys(d["貼文關鍵字："])  # 尋找輸入匡後輸入excel表中的關鍵字
            keywords = d["貼文關鍵字："]
            self.wait()
            self.find_element(*self.post_keyword_button).click()
            self.wait()
            answer = self.logicGame(keywords)
            print(answer)
            for i in range(2, 22):
                for j in range(0, 1):
                    print(str(answer) + '//////' + self.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[3]/div[' + str(i) + ']/div/div[1]/div[1]/p').text)
                    try:
                        answer[j] in self.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[3]/div[' + str(i) + ']/div/div[1]/div[1]/p').text
                        print('此粉專有關鍵字!!!!!!')
                    except:
                        print('此粉專沒有關鍵字')
    
    # 網紅熱門排行，先選擇平台，在選擇粉絲數，最後切換tab
    def kolHotRank(self):
        # self.find_element(*self.close_popup).click()
        # self.find_element(*self.close_popup).click()
        self.find_element(*self.go_to_kol_search).click()
        self.find_element(*self.go_to_kol_search).click()
        self.implicitly_wait()
        self.find_element(*self.kol_hot_rank).click()
        self.implicitly_wait()
        for i in range(1, 4):
            self.find_element(*self.platform_button).click()
            self.implicitly_wait()
            self.find_element(By.XPATH, '//*[@id="menu-platformId"]/div[3]/ul/li[' + str(i) + ']').click()
            self.implicitly_wait()
            for j in range(1, 9):
                self.find_element(*self.fans_button).click()
                self.free_wait(1)
                self.find_element(By.XPATH, '//*[@id="menu-levelId"]/div[3]/ul/li[' + str(j) + ']').click()
                self.implicitly_wait()
                for k in range(1, 7):
                    self.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[3]/div[1]/div[2]/div[1]/div[' + str(k) + ']/span').click()
                    self.free_wait(2)
                    # 找到表格的 tbody 元素
                    tbody_element = self.find_element(*self.topic_rank_tbody)
                    # 找到 tbody 元素底下的所有 tr 元素
                    tr_elements = tbody_element.find_elements(By.TAG_NAME, "tr")
                    # 計算 tr 元素的數量
                    num_of_tr_elements = len(tr_elements)
                    print("tbody 底下有", num_of_tr_elements, "個 tr 元素")
                    top_number = self.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[4]/h3').text
                    top_number = self.change_to_int(top_number)
                    for l in range(2, num_of_tr_elements+1):
                        lower_number = self.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[3]/div[2]/div[1]/table/tbody/tr[' + str(l) + ']/td[4]/h3').text
                        lower_number = self.change_to_int(lower_number)
                        print('目前的top_number: ' + str(top_number) + '目前的lower_number: ' + str(lower_number))
                        if top_number >= lower_number:
                            top_number = lower_number
                        else:
                            small_title = self.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/div[3]/div[2]/div[1]/table/tbody/tr[' + str(l) + ']/td[3]/div/div/h6').text
                            assertAnalysisError(small_title)
                    self.free_wait(1)
    
    def logicGame(self, input_str):
        result = []  # 用於存儲結果的列表
        print(input_str)
        # 使用正則表達式擷取 '{' 和 '}' 之間的內容
        if '{' in input_str:
            # 找到 '}' 的索引
            end_index = input_str.find('}')
            if end_index != -1:
                # 使用正則表達式匹配大括號中的內容
                match = re.search(r'\{(.*?)\}', input_str)
                if match:
                    # 從匹配中獲取大括號中的內容
                    pattern = match.group(1)
                    print(pattern)
                else:
                    print("未找到大括號中的內容")
                if ' and ' in pattern:
                    # 使用 " and " 作為分隔符，將字串分割為兩個子字串
                    substrings = pattern.split(" and ")
                    # 檢查分割後的子字串
                    if len(substrings) == 2:
                        first_part = substrings[0]
                        second_part = substrings[1]
                        print("第一部分:", first_part)
                        print("第二部分:", second_part)
                        ans = first_part + ', ' + second_part
                        result.append(ans)
                    else:
                        print("無法正確分割字串。")
                elif ' or ' in pattern:
                    # 使用 " or " 作為分隔符，將字串分割為兩個子字串
                    substrings = pattern.split(' or ')
                    print(str(substrings))
                    result.append(substrings[0])
                    result.append(substrings[1])
                    print('316: ' + str(result))
            else:
                print('這不在測試範圍內XDD')
            after_brace = input_str[end_index + 1:]
            print('after_brace: ' + after_brace)
            if ' and ' in after_brace:
                suffix = ", "
                substrings = after_brace.split(" and ")
                result = [item + suffix + substrings[1] for item in result]
                print('325: ' + str(result))
            elif ' or ' in after_brace:
                substrings = after_brace.split(" or ")
                result.append(substrings[1])
        else:
            if ' and ' in input_str:
                # 使用 " and " 作為分隔符，將字串分割為兩個子字串
                substrings = input_str.split(" and ")
                # 檢查分割後的子字串
                if len(substrings) == 2:
                    first_part = substrings[0]
                    second_part = substrings[1]
                    print("第一部分:", first_part)
                    print("第二部分:", second_part)
                    ans = first_part + ', ' + second_part
                    result.append(ans)
            elif ' or ' in input_str:
                # 使用 " or " 作為分隔符，將字串分割為兩個子字串
                substrings = input_str.split(" or ")
                result.append(substrings[0])
                result.append(substrings[1])
        return result
        

    def test(self):
        # 過度時期
        self.wait()
        self.find_element(*self.close_popup).click()
        self.find_element(*self.close_popup).click()
        self.wait()
        self.find_element(*self.go_to_kol_search).click()
        self.refresh()
        self.find_element(*self.kol_name_input).click()
        self.find_element(*self.kol_name_input).send_keys("joeman")
        self.wait()
        self.find_element(*self.search_button).click()
        self.wait()

        # 開始驗證聲量分析
        self.find_element(*self.click_first_kol).click()
        self.wait()
        self.switch_to_window()
        self.close()
        self.wait()
        self.switch_to_window()
        self.find_element(*self.ai_smart_search).click()
        self.wait()
        print('ok')