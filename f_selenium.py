# -*- coding:UTF-8 -*-
import time
from selenium import webdriver

path = r'F:\qfPython_codes\ThirdWorkspace\day05\chromedriver.exe'
# 创建浏览器对象
brower = webdriver.Chrome(path)
url = 'https://www.baidu.com/'
brower.get(url)

# 找到百度页面的文本输入框
baidu_input = brower.find_element_by_id('kw')
# 向文本输入框中写入内容
baidu_input.send_keys('美女')
time.sleep(3)
#找到百度的按钮
btn = brower.find_element_by_id('su')
btn.click()
# 找到指定图片进行点击,只能点击按钮，图片需要获取链接通过get

#关闭浏览器
time.sleep(3)
brower.quit()
















