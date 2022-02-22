#! python3

import sys
import urllib.request
import re
import os
import time

url = "http://www.x81zw.com/book/0/668/"
request = urllib.request.Request(url,timeout = 60)
response = urllib.request.urlopen(request)
data = response.read()
data = str(data)

pattern = re.compile(r'(?<=/book/0/668/)\d+(?=\.html)')

geturl = pattern.findall(data)
# 去除第一个有问题的数据
geturl = geturl[1:]

# 获取所有网站URL地址放入get_url.txt中
f = open(r'C:\Users\84534\Desktop\get_url.txt', 'w+')
for u in geturl:
    line = 'http://www.x81zw.com/book/0/668/' + u + '.html' + '\n'
    f.write(line)
f.close()

# 从相应网站爬取文本
def spider(page_url):
    req = urllib.request.Request(page_url)
    response = urllib.request.urlopen(req)
    page = response.read()
    page = page.decode('gbk')                            # 该网站以gbk编码
    f = open(r'C:\Users\84534\Desktop\webpage.txt','w+')
    f.write(page)
    f.close()

# 修饰函数
def modify():
    f_in = open(r'C:\Users\84534\Desktop\万古天帝.txt','a+')
    with open(r'C:\Users\84534\Desktop\webpage.txt','r') as f_out:
        read = f_out.read()
    # 获取文本
    pattern = re.compile(r'(?<=<div id="content">).+(?=</div>)')
    get = pattern.findall(read)
    get = str(get)
    get = re.sub('&nbsp;&nbsp;&nbsp;&nbsp;','\t',get)
    get = re.sub('<br /><br />','\n',get)
    get = get[2:-2]
    get = get + '\n' + '\n'

    # 获取章节标题
    pattern_t = re.compile(r'(?<=<h1>).+(?=</h1>)')
    title = pattern_t.findall(read)
    title = str(title)
    title = title[2:-2]
    title = title + '\n'

    f_in.write(title)
    f_in.write(get)
    f_in.close()

# 从网站导入到 webpage.txt，再从 webpage 加入到 万古天帝.txt 中
with open(r'C:\Users\84534\Desktop\get_url.txt', 'r') as f_geturl:
    url_get = f_geturl.readlines()
for each_url in url_get:
    spider(each_url)
    modify()
    time.sleep(0.075)
    