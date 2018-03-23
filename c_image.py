# -*- coding:UTF-8 -*-

import urllib.request
import urllib.parse


url = 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2699817650,1238409640&fm=27&gp=0.jpg'

#爬取的时候需要一个头部，自己添加
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2'
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)

with open('naza.jpg', 'wb') as f:
    f.write(response.read())
