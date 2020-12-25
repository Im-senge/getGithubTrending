#!/usr/bin/env python
# coding=utf-8
"""
    Project @ Python 爬取GitHub
    Copyright @ 森哥
    Version @ 1.1
    Updated @ 支持用户选择是否克隆数据
              用户可以直观的看到项目的开发者ID和项目名
    Date @ Dec. 22nd. 2020
"""
# 引用BeautifulSoup函数库
from bs4 import BeautifulSoup
# 引用urllib.request函数库，请求数据
import urllib.request
# 引用re函数库，使用正则表达式匹配数据
import re
# 引用os函数库，调用系统命令
import os
# 引用time函数库，保证程序运行时不会被系统检测
import time
# 定义url
url = 'https://github.com/trending'
# 伪装成浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
# 访问请求
req = urllib.request.Request(url=url, headers=headers)
res = urllib.request.urlopen(req)
# 设置浏览器为unicode-8编码
html = res.read().decode('utf-8')
# 声明BeautifulSoup函数
soup = BeautifulSoup(html, "html.parser")
# 用BeautifulSoup检索数据
devData = soup.select(
    'body > div.application-main > main > div.explore-pjax-container.container-lg.p-responsive.pt-6 > div > div > article > h1 > a')
# 依次读取数据
for devProj in devData:
    # 抓取关键字
    devResult = {'title': devProj.get_text()}
    # 用正则表达式去除关键字
    devResult = str(devResult).split('\\n')
    devResult = re.sub('\s|\[\"\{\'title\':', '', str(devResult))
    devResult = re.sub('\s|[\"\'\},\[\]]', '', str(devResult))
    # 生成链接
    devLink = 'https://github.com/' + devResult + '.git'

    # 用split进一步提取开发者ID和项目名称
    spliting = devResult.split("/")
    devName = "{}".format(spliting[0])
    projName = "{}".format(spliting[-1])

    # 捕获开发者和项目数据，让用户自行决定是否获取源码
    print("开发者：" + devName + "\n-----------------------\n项目名称：" + projName + "\n-----------------------\n是否克隆？<y/n>")
    cfm = input()
    if cfm != 'Y' and cfm != 'y':
        print("跳过爬取" + devLink)
    else:
        # 克隆前提示
        print('正在准备克隆')
        # 克隆
        os.system('git clone ' + devLink)
    # 用input实现按任意键继续，类似于C语言的getch()
    input("请按任意键继续")
    # 用clear清除屏幕，类似于C语言的system("cls")
    os.system("clear")
    # 为了防止爬取过快，每条数据访问时间间隔3秒
    time.sleep(3)
    # 注：由于每一页数据有限，不会无限获数据。
