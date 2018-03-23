

1、xpath实例
	图片http://sc.chinaz.com/tupian/
		第一页：http://sc.chinaz.com/tupian/xingganmeinvtupian.html
		第二页：http://sc.chinaz.com/tupian/xingganmeinvtupian_2.html
		第三页：http://sc.chinaz.com/tupian/xingganmeinvtupian_3.html
		懒加载机制：为了提高用户体验和节省带宽，如果一张网页中有100张图片，那么仅仅显示在用户面前的图片会给用户加载，其它图片必须等到用户滚动滚动条的时候，出现在用户面前再去加载这个图片，这种机制就叫做懒加载
		实现原理：一般img标签里面的src属性会动态添加，默认写的是src2属性，图片地址会事先写到src2里面
	内涵段子http://neihanshequ.com/
		注意事项在代码中
2、jsonpath（了解）
	http://blog.csdn.net/luxideyao/article/details/77802389
	import json
	json.dumps() : 将对象转化为json格式字符串
	json.loads() ：将json格式字符串转化为python对象
	json.dump() ：将对象转化为json格式并且写入到文件中
	json.load() ：从文件中读取json格式字符串转化为对象
	
	jsonpath就是类比xpath发明的一套路径表达式，和xpath类似，但是xpath是用来解析xml格式数据的，但是jsonpath是用来解析json格式数据的
	安装：pip install jsonpath   必须国内源下安装，否则出错
	简单使用见代码
3、selenium、phantomjs
	selenium : 就是一套扩展库，需要首先安装，安装完之后，就可以通过selenium这个扩展库里面的函数去操作你的浏览器，让你的浏览器自动化的做一些工作
	安装：pip install selenium
	使用：让selenium来操作谷歌浏览器，首先下载一个对应的谷歌浏览器的驱动，然后让selenium操作这个驱动来达到控制浏览器的目的
	http://chromedriver.storage.googleapis.com/index.html
	http://blog.csdn.net/huilan_same/article/details/51896672
	browser.get()
	browser.back()
	browser.forward()
	
	# 获取一个对象
	find_element_by_id  
	
	# 下面复数类型，获取的都是列表   
	find_elements_by_name
	find_elements_by_xpath  
	find_elements_by_tag_name
	find_elements_by_class_name
	find_elements_by_css_selector  
	find_elements_by_link_text
	
	phantomjs：
		是一个浏览器，是一个无界面的浏览器，可以通过selenium+phantomjs去请求网页，因为phantomjs是一个真实的浏览器，所以可以执行网页中的一些js代码，然后获取执行js代码后的网页内容，然后再通过xpath或者bs4去采集你的内容
	常用功能：
	（1）模拟浏览器滚动条滚动到底部
		js = 'document.body.scrollTop=10000'
		browser.execute_script(js)
	（2）模拟点击加载更多
		见代码9
	（3）模拟滚动滚动条，执行js代码
		见代码10
4、高级登录