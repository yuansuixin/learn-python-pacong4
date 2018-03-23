# -*- coding:UTF-8 -*-

from selenium import webdriver

import time

path = r'F:\qfPython_codes\ThirdWorkspace\day05\phantomjs-2.1.1-windows\bin\phantomjs.exe'
#创建浏览器
browser = webdriver.PhantomJS(path)


url = 'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action='
browser.get(url)
time.sleep(2)
browser.save_screenshot('douban1.png')

js = 'document.body.scrollTop=10000'
browser.execute_script(js)
time.sleep(3)
browser.save_screenshot('douban2.png')
browser.quit()













