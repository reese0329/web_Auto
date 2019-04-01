from util.ClientSelenium import *
import unittest
from util import log
_logger = log.logger('LoginTesterHome')


client = ClientSelenium()
class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        client.get_driver("Ch","https://www.baidu.com")
        time.sleep(2)
        log._logger.info("启动浏览器成功")

    @classmethod
    def tearDownClass(cls):
        client.quit()

    def test_login(self):
        client.start("https://map.baidu.com/","https://www.baidu.com")
        # client.click_element("id=>sole-input")
        time.sleep(2)

    def test_send_keys(self):
        client.send_keys_("id=>sole-input","清河派出所")
        client.click_element("id=>search-button")
        client.get_windows_img (r"D:\sdk\tools\web_Auto\pic\login.jpg")
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()