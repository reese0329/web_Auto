
from Config.setting import *

BaseDir ="D:/sdk/tools/web_Auto/Report"  #从setting 文件导入拼接

class TimeUtil(object):

    def set_date(self): #固定写法
        now = datetime.datetime.now()
        return "{0}-{1}-{2}".format(now.year, now.month, now.day)

    def set_time(self):#固定写法
        return time.strftime("%H-%M")

    def get_report_path(self): #核心函数
        "格式月日/单位时间格式的.html，只用到time"
        nowtime = time.localtime() #转换为可读的
        dir_date = time.strftime('-%Y%m%d', nowtime) #格式化 Report-年月日
        if not os.path.exists(BaseDir + dir_date): #="E:\selenium_uses\\Report-年月日" 文件夹
            os.mkdir(BaseDir + dir_date)
            #print("路径===》",BaseDir + dir_date)
        day_file = time.strftime('%H%M%S', nowtime)
        return BaseDir + dir_date + '\\' + 'Report-' + day_file + '.html'


# https://tieba.baidu.com/index.html
# 修改路径在这里修改

# from util.ParserConfig import ParserConfig
# pc =ParserConfig("D:\selenium_uses\Conf\config.ini")

from selenium import webdriver

class Base(object):
    def chrome_path(self):
        "谷歌的浏览器驱动"
        #读取驱动
        return self.webdriver.Chrome() #把driver目录拷贝到一级目录下。

    def firefox_path(self):
        "火狐的浏览器驱动"
        return self.webdriver.Firefox()
