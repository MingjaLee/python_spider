#!/usr/bin/env python
#coding:utf-8

import urllib
import urllib2
import re


def main():
	page = 1
	url = 'http://www.qiushibaike.com/hot/page/' + str(page)
	user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2)'
	headers = { 'User-Agent' : user_agent }
	try:
	    request = urllib2.Request(url,headers = headers)
	    response = urllib2.urlopen(request)
	    content = response.read().decode('utf-8')
	    pattern = re.compile('<div class="author.*?clearfix">.*?<h2>(.*?)</h2>.*?' + 
	    	'<div class="content.*?<span>(.*?)</span>.*?</a>(.*?)<div class="stats".*?class="number">(.*?)</i>', re.S)
	    # pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
	    #                      'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
	    items = re.findall(pattern,content)
	    # print 'len(items):', len(items)
	    # return
	    cnt = 0
	    for item in items:
	        haveImg = re.search("img",item[2])
	        if not haveImg:
	            print item[0]
	            print item[1]
	            print item[3] + '\n'
	            cnt +=1
	    print cnt
	except urllib2.URLError, e:
	    if hasattr(e,"code"):
	        print e.code
	    if hasattr(e,"reason"):
	        print e.reason

if __name__ == "__main__":
	main()