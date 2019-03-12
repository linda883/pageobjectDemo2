from page_objects import PageElement
from selenium import webdriver
from pages.BaseLoginPage import LoginPage
import unittest
import time


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path='/Users/lindafang/PycharmProjects/postepbystep/testcases/chromedriver')
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.login_page = LoginPage(cls.driver)
        cls.login_page.get('http://www.baidu.com')

    def test_login(self):
        self.login_page.username
        self.login_page.username2

        LoginPage.username
        self.login_page.user3.f
        x=PageElement()




        self.login_page.password.send_keys("sdf")
        self.login_page.login_button.click()


    @classmethod
    def tearDownClass(cls):
        print('\ntest complete!')
        # Closes the current window.
        # 关闭当前窗口。
        cls.driver.close()
        # Quits the driver and closes every associated window.
        # 退出驱动并关闭所有关联的窗口。
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
