from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import unittest
#添加断言

from util import log
_log = log.logger("WebTest")

class LoginBaidu(unittest.TestCase):


    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()
        _log.info("open!")

        self.driver.find_element_by_css_selector("#u1 > a.lb").click()
        sleep(2)  #添加等待时间，等待弹窗展示

        #
        # a = self.driver.find_element_by_class_name("pass-form-logo").text  #登录弹窗展示，不能获取文本信息
        # self.assertEqual("扫码登录",a,msg="当前弹窗应为{}，实际为{}".format("扫码登录",a))


        # sleep(1)
        #
        self.driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()

        #用户名密码登录
        self.driver.find_element_by_id("TANGRAM__PSP_10__userName").clear()
        self.driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("13426257806")
        self.driver.find_element_by_id("TANGRAM__PSP_10__password").clear()
        self.driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("13426257806")
        self.driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
        sleep(3)

        self.driver.find_element_by_id("TANGRAM__39__button_send_mobile").click()
        keys = input("输入验证码：")
        # driver.find_element_by_id("TANGRAM__39__input_label_vcode").clear()  #不能获取验证码输入框
        # driver.find_element_by_id("TANGRAM__39__input_label_vcode").send_keys(keys)
        # sleep(3)
        self.driver.find_element_by_id("TANGRAM__39__button_submit").click()
        print("login!")
        sleep(4)

        # #短信验证码登录
        # driver.find_element_by_id("TANGRAM__PSP_10__smsSwitchWrapper").click()
        # driver.find_element_by_id("TANGRAM__PSP_10__smsPhone").clear()
        # driver.find_element_by_id("TANGRAM__PSP_10__smsPhone").send_keys("13426257806")
        # code = driver.find_element_by_id("TANGRAM__PSP_10__smsTimer").click()
        # keys = input("输入验证码：")
        # driver.find_element_by_id("TANGRAM__PSP_10__smsVerifyCode").clear()
        # driver.find_element_by_id("TANGRAM__PSP_10__smsVerifyCode").send_keys(keys)
        # sleep(3)
        # driver.find_element_by_id("TANGRAM__PSP_10__smsSubmit").click()
        # print("login!")
