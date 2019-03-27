from selenium import webdriver
import os, time, unittest, configparser
from selenium.webdriver.common.action_chains import ActionChains

class LoginDouban(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 每轮执行case的开始
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.douban.com")
        # cls.driver.implicitly_wait (5)  # 隐式等待5s

    @classmethod
    def tearDownClass(cls):  # 每轮执行case的结束
        print("this is the end!")
        cls.driver.quit()

    # 保护代码
    def test_login(self):
        time.sleep (4)
        try:
            # self.assertEqual("豆瓣", self.driver.title, msg="当前网页的{}和{}一样".format("豆瓣", self.driver.title))
            # self.assertEqual("https://www.douban.com/", self.driver.current_url,
            #                       msg="当前网页的{}和{}一样".format ("https://www.douban.com", self.driver.current_url))
            # obj = self.driver.__sizeof__()
            # print(obj)
            # time.sleep(2)
            # if int(obj / 1024) > 60:
            #     print(self.driver.current_url,"网页过大")
            #     #     fp = open("../test/sizelog.txt", "w", encoding="utf-8")  # 自己封装,拼接路径，w-写入
            #     #     fp.write(get_ini_date("Language", "size").format(self.driver.current_url))  #写入内容
            #     # #     fp.close()
            xf = self.driver.find_element_by_xpath("//*[@id='anony-reg-new']/div/div[1]/iframe")
            ts = self.driver.switch_to.frame(xf)
            check_login = self.driver.find_element_by_class_name("account-tab-account")
            time.sleep(5)
            if check_login.is_enabled():
                self.assertEqual("密码登录", check_login.text, msg="登录element{}".format(check_login.text))
            else:
                raise "{}不可点击".format(check_login.text)
            check_login.click()
            time.sleep(5)
        except Exception as err:
            print(format(err))


if __name__ == '__main__':
    unittest.main()
