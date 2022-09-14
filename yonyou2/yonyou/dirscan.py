#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import sys
import threading

RED = '\x1b[1;91m'
BLUE = '\033[1;94m'
GREEN = '\033[1;32m'
BOLD = '\033[1m'
ENDC = '\033[0m'


def show():
    print(RED + '''
                           _  _                                
                         __| |(_) _ __   ___   ___  __ _  _ __  
                       / _` || || '__| / __| / __|/ _` || '_ \ 
                      | (_| || || |    \__ \| (__| (_| || | | |
                       \__,_||_||_|    |___/ \___|\__,_||_| |_|
                                                               
    Title: CNVD-2021-30167 用友NC BeanShell RCE
    Version: NC6.5
    Author: HUGH
    ''' + RED)


def open_url():
    with open(target, "r") as fp:  # 文件读取
        s1 = fp.read()
    lis = list(s1.split("\n"))
    return lis


def open_mulu():
    with open(add, "r") as fp:  # 文件读取
        s2 = fp.read()
    lia = list(s2.split("\n"))
    return lia


def scan():
    for path in lia:  # 遍历组合url路径
        for addr in lis:
            new_url = addr + path
            print(BLUE + '\n[*]正在检测漏洞是否存在\n' + ENDC, end='')
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/90.0.4430.93 Safari/537.360',
                'Content-Type': 'application/x-www-form-urlencoded'}

            try:
                response = requests.get(url=new_url, headers=headers, timeout=3)
                if response.status_code == 200 and 'BeanShell' in response.text:
                    sys.stdout.write('\r' + '[+]%s\t\t\n' % new_url)
                    result = open('result1.html', 'a+')
                    result.write(
                        '<a href="' + new_url + '" rel="external nofollow" target="_blank">' + new_url + '</a>')
                    result.write('\r\n</br>')
                    result.close()
                    print(GREEN + '[+]BeanShell页面存在, 可能存在漏洞: {}'.format(new_url) + ENDC, end='')
                else:
                    print(RED + '[-]漏洞不存在!' + ENDC, end='')
            except:
                print(RED + '[-]无法与目标建立连接!' + ENDC, end='')


if __name__ == '__main__':
    target = "url.txt"  # 测试目标
    add = "Vuln_url.txt"  # 需要添加到url末尾的路径
    time = 5  # 连接超时时长,秒
    state = 200  # 匹配的状态码，符合时才会将url写入文件
    open_url()
    open_mulu()
    lis = open_url()
    lia = open_mulu()
    show()
    scan()
    print("\n")
    print(RED + "[*]扫描结束，结果已输出到results.html中！" + ENDC, end='')
