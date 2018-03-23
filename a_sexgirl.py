# -*- coding:UTF-8 -*-

import urllib.request
from lxml import etree
import os


class SexGirl(object):
    def __init__(self, start, end, url):
        self.start = start
        self.end = end
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2'
        }

    def run(self):
        for page in range(self.start, self.end+1):
            print('开始下载第%s页'%page)
            request = self.handle_request(page)
            self.download_image(request)
            print('结束下载第%s页'%page)

    def handle_request(self, page):
        if page==1:
            url = self.url % ''
        else:
            url = self.url%('_'+str(page))
        request = urllib.request.Request(url=url,headers=self.headers)
        return request


    def download_image(self, request):
        response = urllib.request.urlopen(request)
        tree = etree.HTML(response.read())
        ret = tree.xpath('//div[@id="container"]//img/@src2')
        dirname = 'sex'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        for image_url in ret:
            image_name = os.path.basename(image_url)
            image_path = os.path.join(dirname,image_name)
            urllib.request.urlretrieve(image_url,image_path)



def main():
    start = 1
    end = 2
    url = 'http://sc.chinaz.com/tupian/xingganmeinvtupian%s.html'

    obj = SexGirl(start, end, url)
    obj.run()


if __name__ == '__main__':
    main()
