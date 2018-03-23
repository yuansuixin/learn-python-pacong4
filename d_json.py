# -*- coding:UTF-8 -*-
import json


lt = [

    {'name':'aaa','age':18,'height':187},
    {'name':'bbbb','age':18,'height':187},
    {'name':'ddd','age':18,'height':187},
    {'name':'ssss','age':18,'height':187},
    {'name':'eee','age':18,'height':187},
    {'name':'中国','age':18,'height':187},

]


json.dump(lt,open('text.txt','w',encoding='utf-8'),ensure_ascii=False)
obj = json.load(open('test.txt',encoding='utf-8'))
print(obj)






