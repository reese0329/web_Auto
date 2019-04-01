# -*- coding: utf-8 -*-
'a practice of ...'

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC  # 显示等待
from selenium.webdriver.support.ui import WebDriverWait  # 显示等待
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #键盘类
import time

# from util.Base import Base
#
# base = Base()

# 定位器字典 把value打包
locatorTypeDict = {
    'xpath': By.XPATH,
    'css': By.CSS_SELECTOR,
    'id': By.ID,
    'name': By.NAME,
    'className': By.CLASS_NAME,
    'tagName': By.TAG_NAME,
    'link': By.LINK_TEXT,
    'parLink': By.PARTIAL_LINK_TEXT
}

from selenium import webdriver


# 只开放了基础api的，定位器请自己学习封装完成作业，下节课在讲带保护的高级封装
class ClientSelenium(object):
    """通过封装把Page的行为压缩在这里"""

    def get_driver(self, driver, url):
        "初始化浏览器和打开目标url"
        if driver == 'firefox' or driver == 'Firefox' or driver == 'F' or driver == 'f':
            # exe_path = base.firefox_path()#第二个功能是包裹在第一个功能下面的
            self.driver = webdriver.Firefox()
        elif driver == 'Chrome' or driver == 'chrome' or driver == 'Ch' or driver == 'ch':
            # exe_path = base.chrome_path()
            self.driver = webdriver.Chrome()
            print("拉起浏览器成功")
        else:
            print("输入在预期以外")
        self.driver.get(url)  # 区域3
        return self.driver

    def start(self, url, _url):
        """
        不拉起浏览器打开网页
        :param url: 打开网页
        :param _url: 期望网页
        :return:
        """
        self.driver.get(url)
        self._get_current_url(_url)

    def assert_title(self, titleText):
        """
        页面标题上是否包含关键字,支持传入多个参数
        :param titleStr: 关键字
        :param args: 支持传入多个参数
        :return:布尔
        """
        try:
            assert titleText in self.driver.title, \
                "在title里没有找到%s" % titleText
            print("加载网页正确")  # 业务self.assertTrue()
            return True
        except Exception as error:
            print(format(error))
            return False

    def assert_source(self, sources):
        """
        网页源码是否包含关键字 做业务判断
        :param sources: list [arg1,arg2...]
        :return:
        """
        for source in sources:  # 关键字驱动有可能包含多个参数
            try:
                assert source in self.driver.page_source, \
                    "在page_source里没有找到%s" % source
                print("判断 %s 包含在page_source" % source)
            except AssertionError as error:  # 断言表达式
                print(format(error))
            except Exception as error:
                print(format(error))

    time_wait = 2

    def time_sleep(self, time_wait):
        """
        强制等待默认为2秒
        :param time_wait:
        :return:
        """
        if time_wait <= 0:
            time.sleep(time_wait)
        else:
            print("等待%ss" % time_wait)
            time.sleep(time_wait)

    def max_size(self):
        """
        放大浏览器最大化 需要先拉起浏览器
        :return:
        """
        time.sleep(0.5)  # 切换展示
        self.driver.maximize_window()

    def set_size(self, width=800, height=600):
        """
        先打印浏览器尺寸，设置浏览器到尺寸
        :param width: 宽
        :param height: 高
        :return:
        """
        self.driver.set_window_size(width, height, windowHandle="current")  # 当前句柄
        print("尺寸设置成功")

    def _get_current_url(self, _url):
        try:
            assert _url == self.driver.current_url
        except Exception as error:
            print(format(error))

    def F5(self, _url):
        """
        刷新后验证网页正确  now_url覆写使用
        :return:
        """
        self.driver.refresh()
        print("刷新正确")
        self._get_current_url(_url)  # 刷新后判断当前网页

    def back(self, _url, time_wait=4):
        """
        后退到之前的页面（等同浏览器上按回退按钮）
        条件：先需要有前后打开的2个页面
        :param _url:形参是验证当前页面
        :param time_wait:属于time_sleep方法
        :return:
        """
        self.time_sleep(time_wait)
        self.driver.back()
        self._get_current_url(_url)
        print("back网页成功")

    def forward(self, _url, time_wait=4):
        """
        配合浏览器回退使用，回到之前的页面
        :param _url:形参是验证当前页面
        :param time_wait:属于time_sleep方法
        :return:
        """
        self.time_sleep(time_wait)
        self.driver.forward()
        self._get_current_url(_url)
        print("forward网页成功")

    def quit(self):
        """关闭浏览器
        :return:
        """
        self.time_sleep(self.time_wait)  # 展示最后一条case
        self.driver.quit()
        # print("关闭浏览器",self.driver.current_window_handle)

    def get_element(self, locator):
        '''
        非显式等待
        driver.get_element("css=>#el")
        '''
        if "=>" not in locator:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = locator.split("=>")[0]
        value = locator.split("=>")[1]

        if by == "id":
            element = self.driver.find_element_by_id(value)
        elif by == "name":
            element = self.driver.find_element_by_name(value)
        elif by == "class":
            element = self.driver.find_element_by_class_name(value)
        elif by == "link_text":
            element = self.driver.find_element_by_link_text(value)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(value)
        elif by == "css":
            element = self.driver.find_element_by_css_selector(value)
        elif by == "tag_name":
            element = self.driver.find_element_by_tag_name(value)
        else:
            raise NameError(
                "不在选择范围内,'id','name','class','link_text','xpath','css','tag'.")
        return element

    def get_element_wait(self, locator, timeout=12, poll=0.5):
        '''
        单个元素的显式等待，接收参数更少（可以不直接使用）
        driver.element_wait("css=>#el", 10)
        :param xpath:
        :param poll:不填写则默认0.5秒
        :param timeout:默认12秒
        '''
        if "=>" not in locator:
            raise NameError("Positioning syntax errors")
        # #main > div.row > div.sidebar.col-md-3 > div:nth-child(1) > div > a
        # by=>value
        #
        by = locator.split("=>")[0]      #以==>分别切割 左边
        value = locator.split("=>")[1]   #分别切割 右边

        if by == "id":
            element = WebDriverWait(self.driver, timeout, poll).until(EC.presence_of_element_located((By.ID, value)))
        elif by == "name":
            element = WebDriverWait(self.driver, timeout, poll).until(EC.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            element = WebDriverWait(self.driver, timeout, poll).until(
                EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            element = WebDriverWait(self.driver, timeout, poll).until(
                EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            element = WebDriverWait(self.driver, timeout, poll).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            element = WebDriverWait(self.driver, timeout, poll).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        elif by == "tag":
            element = WebDriverWait(self.driver, timeout, poll).until(
                EC.presence_of_element_located((By.TAG_NAME, value)))
        else:
            raise NameError(
                "不在选择范围内,'id','name','class','link_text','xpaht','css','tag'.")
        return element

    def get_elements_wait(self, locator, timeout=12, poll=0.5):
        '''
        多个元素的显式等待，接收参数更少（可以不直接使用）
        driver.element_wait("css=>#el", 10)
        :param xpath:
        :param poll:不填写则默认0.5秒
        :param timeout:默认12秒
        '''
        if "=>" not in locator:
            raise NameError("Positioning syntax errors")
        # #main > div.row > div.sidebar.col-md-3 > div:nth-child(1) > div > a
        # by=>value
        #
        by = locator.split("=>")[0]
        value = locator.split("=>")[1]

        if by == "id":
            element = WebDriverWait(self.driver, timeout, poll).until(EC.presence_of_all_elements_located((By.ID, value)))
        elif by == "name":
            element = WebDriverWait(self.driver, timeout, poll).until(EC.presence_of_all_elements_located((By.NAME, value)))
        elif by == "class":
            element = WebDriverWait(self.driver, timeout, poll).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            element = WebDriverWait(self.driver, timeout, poll).until(
                EC.presence_of_all_elements_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            element = WebDriverWait(self.driver, timeout, poll).until(EC.presence_of_all_elements_located((By.XPATH, value)))
        elif by == "css":
            element = WebDriverWait(self.driver, timeout, poll).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, value)))
        else:
            raise NameError(
                "不在选择范围内,'id','name','class','link_text','xpaht','css'.")
        return element


    def get_window_handle(self):
        """
        网页句柄
        :param num:
        :return:
        """
        handles = self.driver.window_handles
        #self.driver.switch_to.window(handles[num])



        return handles

    def leave_frame(self):
        """
        将焦点切换到默认框架(iframe)
        """
        self.driver.switch_to.default_content()

    def submit(self, locator):
        """
        提交
        driver.submit("xpath=>value")
        """
        self.time_sleep(self.time_wait)
        self.get_element_wait(locator)  # 显式等待
        self.get_element(locator).submit()  # 当显示等待触发后在提交
        print('确认元素%s后提交了' % locator)

    def get_windows_img(self, file_path):
        """
        截图
        file_path:自己拼接
        driver.get_windows_img("绝对路径/testcase名称.jpg")
        """
        self.time_sleep(3)
        self.driver.get_screenshot_as_file(file_path)
        print('获得截图.')



    def js_execute(self, script, *args):
        """
        执行js脚本  *args为不定长 元祖
        使用方法：
        driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script, *args)
        print('Execute script: %s' % (script))

    def check_element(self, locator, text):
        """
        定位检查后在输出
        :Usage:
        driver.type("xpath=>//*[@id='el']", "selenium")
        """
        self.get_element(locator)  #
        el = self.get_element_wait(locator)  # 双保险
        try:
            time.sleep(1)
            el.clear()
        except:
            print('clear failed is %s' % locator)
        el.send_keys(text)
        time.sleep(1)
        print('check 元素%s is %s' % (text, locator))

    def click_element(self, locator=None):
        """
        点击页面元素
        driver.clickinfo("xpath=>//*[@id='el']")
        """
        if locator:  # 定义了None
            self.get_element_wait(locator)
            el = self.get_element(locator)
            el.click()
            print("已选择对象:", locator)
            # locator=None
            # return locator
        else:
            # .click()单击
            ActionChains(self.driver).click().perform()  # 不会立即执行 按顺序位

    def send_keys_(self, locator, context):
        '''
        输入内容
        :param pattern: 元素定位方法，id，name等
        :param position: 定位元素的value
        :param context: 要输入的内容
        :return:
        '''
        try:
            element = self.clear_(locator)
            if element:
                element.send_keys(context)
                return element
        except Exception as error:
            print(error)

    def get_window_handle(self):
        """
        返回当前网页句柄
        :return:
        """
        return self.driver.current_window_handle

    def click_partial(self, text):
        """
        可以局部也可以全局
        driver.click_text("新闻")
        """
        self.time_sleep(self.time_wait)
        self.driver.find_element_by_partial_link_text(text).click()
        print('打开%s link' % text)

    def clear_(self, locator):
        '''
        清空元素内容
        :param pattern: 元素定位方法， id， name等
        :param position: 定位元素的value
        :return:
        '''
        try:
            element = self.get_element(locator)
            if element:
                # print(element.text)
                element.click()  #
                # element.clear()
            return element
        except Exception as error:
            print(error)

    def double_click(self, locator):
        """
        双击元素
        driver.double_click("xpath=>")
        """
        a = self.get_element_wait(locator)
        el = self.get_element(locator)
        ActionChains(self.driver).double_click(el).perform()
        print('双击元素:', locator)

    def get_attribute(self, xpath, value):
        """
        拿到元素 可以结合之前代码查看
        driver.get_attribute("xpath=>定位器", "type")
        """
        self.time_sleep(self.time_wait)
        self.get_element_wait(xpath)
        ele = self.get_element(xpath)
        attr_value = ele.get_attribute(value)  # get_attribute是API  attr元素el的属性
        if attr_value:
            print('attribute_value %s is: %s' % (value, attr_value))
            return attr_value
        else:
            print('not found attribute_value: %s' % value)
            return None  # 布尔

    def get_link_text(self, locator):
        '''
        获取元素内容 注意并不是所有的元素都会有text
        driver.get_link_text("link=>value")
        :param pattern: 鼓励只用超文本的
        :param position: 定位元素的value
        :return:
        '''
        try:
            element = self.get_element(locator)  # locator写法在里面了
            # t = element.get_attribute('value')
            text = element.text
            return text
        except Exception as error:
            print(error)

    def switch_frame(self,locatValue=None):
        """

        :param locatValue: 框架元素
        :return:
        """
        if locatValue:
            self.driver.switch_to.frame(locatValue)


    def frame_to_switch(self,target, locatValue, timeout=10):
        """
        显式等待，判断是否需要切换到frame
        :param driver:其他函数的
        :param targetType:用字典的
        :param locatorValue:
        :return:
        """
        wait = WebDriverWait(self.driver, timeout)#这样填充
        try:
            wait.until(EC.frame_to_be_available_and_switch_to_it
                       ((locatorTypeDict[target.lower()], locatValue)))
            print("frame存在，切换成功")
        except Exception as error:
            print(format(error))

    def switch_accept_alert(self):
        """
        确认弹出窗体
        driver.accept_alert()
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        关闭弹出窗体 拒绝
        driver.dismiss_alert()
        """
        self.driver.switch_to.alert.dismiss()
