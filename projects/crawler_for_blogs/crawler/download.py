#!/usr/bin/python3
from assets import useragent
import requests


# 页面下载
def download(url):
    """
    下载指定url页面
    :param url:
    :return:
    """
    headers = {
        'User-Agent': useragent.get_user_agent()
    }
    s = requests.session()
    r = s.request(method='get', url=url, headers=headers)
    if r.status_code == 200:
        print('正在抓取地址:%s' % url)
        print('User-Agent:', r.request.headers.get('user-agent'))
        return True, r.content
    return False, ''
