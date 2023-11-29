from selenium.webdriver.common.by import By
from ..common.page import Page
from selenium.common.exceptions import NoSuchElementException

# 封装的Milelens登入頁

class CathayLoginPage(Page):
    menu = (By.XPATH, '/html/body/div[1]/header/div/div[1]/a/img[2]')
    product_intro = (By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[1]/div')
    credit_card = (By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div')
    credit_content = (By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]')
    card_intro = (By.XPATH, '//*[@id="lnk_Link"]')
    abandon_card = (By.XPATH, '/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]')
    

    def login(self):
        """登入頁"""
        self.implicitly_wait()
        # 設置瀏覽器窗口大小:（宽度 x 高度）
        self.set_window_size(430, 932)  # 這裡設置為手機畫面
        self.wait()
        self.save_screen_shot()
        self.implicitly_wait()
        self.find_element(*self.menu).click()
        self.implicitly_wait()
        self.find_element(*self.product_intro).click()
        self.wait()
        self.find_element(*self.credit_card).click()

        # 設置最大重試次數，error handling
        max_retries = 3
        retry_count = 0
        while retry_count < max_retries:
            try:
                div_element = self.find_element(*self.credit_content)
                break
            except NoSuchElementException:
                print(f"Element not found. Retrying ({retry_count + 1}/{max_retries})...")
                self.free_wait(1)
                retry_count += 1
            if retry_count == max_retries:
                print("Element not found after multiple retries. Exiting.")
        a_elements = div_element.find_elements(By.TAG_NAME, "a")
        print(len(a_elements))
        self.implicitly_wait()
        self.find_element(*self.card_intro).click()
        self.scroll_script("3750")
        self.wait()
        card_div_element = self.find_element(*self.abandon_card)
        span_elements = card_div_element.find_elements(By.TAG_NAME, "span")
        for i in range(1, len(span_elements) + 1):
            self.find_element(By.XPATH, '/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[' + str(i) + ']').click()
            self.implicitly_wait()
            self.save_screen_shot()
            self.wait()