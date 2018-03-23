# -*- coding:UTF-8 -*-
import json
import jsonpath

obj = json.load(open('book.json', encoding='utf8'))
# print(obj)

# 得到所有book的author元素的值
# ret = jsonpath.jsonpath(obj, '$.store.book[*].author')

# 类似于xpath里面的 //author
# ret = jsonpath.jsonpath(obj, '$..author')

# 获取store元素里面的book列表和一个bicycle字典
# ret = jsonpath.jsonpath(obj, '$.store.*')

# 查找store下面所有的price
ret = jsonpath.jsonpath(obj, '$.store..price')

# 查找所有book的，book里面的第二本书，注意，下标从0开始
ret = jsonpath.jsonpath(obj, '$..book[1]')

# 因为下标从0开始，所以最后一本书的下标就是长度-1
ret = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')

# 类似于python里面的切片，取出下标为0和1的前两本书
# ret = jsonpath.jsonpath(obj, '$..book[:2]')

# 查找所有book里面价格小于10 的书籍
ret = jsonpath.jsonpath(obj, '$..book[?(@.price<10)]')

print(ret)

