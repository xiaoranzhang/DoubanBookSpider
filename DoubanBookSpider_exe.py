# !/usr/bin/env python
# _*_ coding:utf-8 _*_

# “豆瓣读书”小说类爬虫

import sys
import urllib
import urllib2
import re
reload (sys)


# 网页页码（5/6/2015止，小说类页码到72270）
# 生成网页后缀pages的页码数组
def pages():
	pages=0
	pages_list=[]
	while pages<72270:
		pages=pages+15
		pages_list.append(pages)
	return pages_list


# 获得网页的url信息: 第一页
def get_url_index(url_index):
	request=urllib2.Request(url_index)
	for key in headers:
		request.add_header(key,headers[key])
		response=urllib2.urlopen(request)
		outcome=response.read()
		decode_outcome_utf8=outcome.decode('utf=8','ignore')
		encode_outcome_gbk=decode_outcome_utf8.encode('gbk','ignore')
	return encode_outcome_gbk
	
# 获得网页url信息：从第二页开始
def get_url(url_2nd):
	request=urllib2.Request(url_2nd)
	for key in headers:
		request.add_header(key,headers[key])
		response=urllib2.urlopen(request)
		outcome=response.read()
		decode_outcome_utf8=outcome.decode('utf=8','ignore')
		encode_outcome_gbk=decode_outcome_utf8.encode('gbk','ignore')
	return encode_outcome_gbk


# 程序入口
# 调用函数
sys.setdefaultencoding('utf-8')
book_list=[]     #建立一个小说的空数组
headers = {
	       "DNT":"1",
	       "Host":"book.douban.com",
	       "User-Agent":"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36"
}

# 豆瓣读书小说类书单的第一页和其他页面的url不同，因此单独获取url路径
url_index="http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/book"
get_url_index(url_index)

# 调用pages()函数，获得豆瓣读书的第2-72270页的url
for url_pages in pages():
	url_2nd="http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/book?start=" + str(url_pages)    
get_url(url_2nd)


