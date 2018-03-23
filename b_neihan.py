# -*- coding:UTF-8 -*-
import json
import urllib.request
import urllib.parse
from lxml import etree

'''
爬取内涵段子

'''
class NeiHan(object):
    def __init__(self,url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2'
        }

    def run(self):
        request = self.handle_request()
        self.download_neihan(request)

    def handle_request(self):
        request = urllib.request.Request(url=self.url,headers=self.headers)
        return request

    def download_neihan(self, request):
        response = urllib.request.urlopen(request)
        #获取到内容，使用xpath查找
        tree = etree.HTML(response.read().decode())
#         首先找到所有的li
        li_list = tree.xpath('//*[@id="detail-list"]/li')
        # li_list 里面存放的都是li对象，这种对象自带了xpath对象
        items = []

        for li in li_list:
            item = {}
            # xpath 加上一个点，表示从当前开始查找
            #这个地方匿名用户的话，结构变了，可能找不到，这个可以单独的处理
            try:
                image_url = li.xpath('.//div[@class="header "]//img/@data-src')[0]
            except Exception as e:
                image_url = '么有头像'
            try:
                name = li.xpath('.//div[@class="header "]/a/div/span[@class="name"]/text()')[0]
            except Exception as e:
                name='匿名用户'
            try:
                time = li.xpath('.//div[@class="header "]/a/div/span[@class="time timeago"]/text()')[0]
            except Exception as e:
                time='none'
            content = li.xpath('.//div[@class="content-wrapper"]//p/text()')[0]
            zan = li.xpath('.//div[@class="options"]/ul/li/span[@class="digg"]/text()')[0]


            item['图片地址'] = image_url
            item['名字']=name
            item['日期']=time
            item['段子']=content
            item['赞']=zan
            items.append(item)
            string = json.dumps(items,ensure_ascii=False)
            with open('beihan.txt','a',encoding='utf-8') as f:
                f.write(string)

def main():
    url = 'http://neihanshequ.com/'
    obj = NeiHan(url)
    obj.run()

if __name__ == '__main__':
    main()

