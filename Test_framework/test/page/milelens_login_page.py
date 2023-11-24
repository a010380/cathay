from selenium.webdriver.common.by import By
from ..common.page import Page

# 封装的Milelens登入頁

class MilelensLoginPage(Page):
    loc_search_input_account = (By.XPATH, '//*[@data-test-id="signInEmail"]/input')
    loc_search_input_password = (By.XPATH, '//*[@data-test-id="signInPassword"]/input')
    loc_search_button = (By.XPATH, '//*[@data-test-id="signInButton"]')

    def login(self, kw1, kw2):
        """登入頁"""
        self.find_element(*self.loc_search_input_account).send_keys(kw1)  # 尋找輸入匡後輸入帳號
        self.find_element(*self.loc_search_input_password).send_keys(kw2)  # 尋找輸入匡後輸入密碼
        self.find_element(*self.loc_search_button).click()  # 尋找登入按鈕後點擊按鈕
