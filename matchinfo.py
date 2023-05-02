#encoding:utf-8
import sys

import requests
import re
import os
from bs4 import BeautifulSoup

import lxml
url = "https://www.baidu.com" #正式获取用

res = requests.get(url)
res.encoding = res.apparent_encoding
soup= BeautifulSoup(res.text,'lxml')
lst = soup.find_all('a')
if(res.status_code == 200):
    print("正常获取")
content_list=[]
for i in lst:
    content = i.get_text().strip()
    content_list.append(content)
    # print(content_list)
    tips_str = '/'.join(content_list)
# print(tips_str)
pattern_tips = re.compile('/(.+?)/')
tips = re.findall(pattern_tips, tips_str)
# print(tips)
if(tips == ['']):
    os.system("python mail.py")
    print("找到了")
    time.sleep() #输入不存在的方法，使其程序报错，终止程序运行
else:
    print("未找到")

