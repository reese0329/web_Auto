from selenium import webdriver
import os, time, unittest, configparser
from selenium.webdriver.common.action_chains import ActionChains

from util import log

_log = log.logger('Testerhome')
# from util.ClientSelenium import *
# client = ClientSelenium()

class LoginDouban(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 每轮执行case的开始
        # client.get_driver("f", "https://www.douban.com")
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://www.douban.com")
        cls.driver.implicitly_wait(5)  # 隐式等待5s
        cls.driver.get_screenshot_as_file(r"D:\sdk\tools\web_Auto\pic\browser.png")
        _log.info("成功打开浏览器！")

    @classmethod
    def tearDownClass(cls):  # 每轮执行case的结束
        print("this is the end!")
        _log.info("关闭浏览器！")
        cls.driver.quit()

    # 保护代码
    def test_login(self):
        time.sleep(4)
        try:
            # self.assertEqual("豆瓣", self.driver.title, msg="当前网页的{}和{}一样".format("豆瓣", self.driver.title))
            # self.assertEqual("https://www.douban.com/", self.driver.current_url,
            #                       msg="当前网页的{}和{}一样".format ("https://www.douban.com", self.driver.current_url))
            # #判断尺寸
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
            _log.info("切换至账号密码登录")
            if check_login.is_enabled():
                self.assertEqual("密码登录", check_login.text, msg="登录element{}".format(check_login.text))
            else:
                raise "{}不可点击".format(check_login.text)
            # client.get_windows_img (r"D:\sdk\tools\web_Auto\pic\login.jpg")
            check_login.click()
            time.sleep(5)
            _log.info("成功切换至账号密码登录")
        except Exception as err:
            self.driver.get_screenshot_as_file(r"D:\sdk\tools\web_Auto\pic\switch.png")
            print(format(err))


    def test_login2(self):
        username = "106078014@qq.com"
        password = "199403291402Trx"
        try:
            self.driver.find_element_by_id("username").send_keys(username)
            time.sleep(1)
            self.driver.find_element_by_id("password").send_keys(password)
            time.sleep(1)
            usnm = self.driver.find_element_by_id("username").get_attribute("value")
            pswd = self.driver.find_element_by_id("password").get_attribute("value")
            print("用户名为{},密码为{}".format(usnm,pswd))
            _log.info("成功输入！")
            self.driver.find_element_by_name("remember").click()
            time.sleep(2)
            #如果跳转到其他网页，仍需再次判断尺寸
            # obj = self.driver.__sizeof__()
            # print(obj)
            # time.sleep(2)
            # if int(obj / 1024) > 60:
            #     print(self.driver.current_url,"网页过大")
            #     #     fp = open("../test/sizelog.txt", "w", encoding="utf-8")  # 自己封装,拼接路径，需要改为a+，否则覆盖
            #     #     fp.write(get_ini_date("Language", "size").format(self.driver.current_url))  #写入内容
            #     # #     fp.close()
            button = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[5]/a")
            if "登录豆瓣" in button.text: #校验是否存在登录按钮，存在则点击
                button.click()
            time.sleep(3)
            self.driver.switch_to.default_content()    #成功登录后，切换表单
            pic = self.driver.find_element_by_css_selector("#db-nav-sns > div > div > div.nav-logo > a") #定位元素
            if pic.is_displayed():  #确认pic是否存在来判断是否成功登录
                print("login success!")
            # cookies = self.driver.get_cookies()  #获取cookies
            # print("url {1}的cookie_name:{0},cookie_value:{2}".format(cookies[0].get("name"),self.driver.current_url,cookies[0].get("value")))
            # time.sleep(1)
            # _log.info("登录成功")
        except Exception as err:
            # client.get_windows_img(r"D:\\sdk\\tools\\web_Auto\\pic\\login.jpg")
            self.driver.get_screenshot_as_file (r"D:\sdk\tools\web_Auto\pic\login_failed.png")
            print(format(err))


    def test_login_quit(self):
        try:
            self.driver.find_element_by_css_selector("#db-global-nav > div > div.top-nav-info > ul > li.nav-user-account > a > span:nth-child(1)").click()
            time.sleep(1)
            self.driver.find_element_by_css_selector("#db-global-nav > div > div.top-nav-info > ul > li.nav-user-account.more-active > div > table > tbody > tr:nth-child(5) > td > a").click()
            time.sleep(5)
            douban = self.driver.find_element_by_css_selector("#anony-nav > h1 > a")
            if douban.is_displayed():
                print("logout sucess!")
            _log.info("成功退出！")
        except Exception as err:
            print(format(err))



if __name__ == '__main__':
    unittest.main()
