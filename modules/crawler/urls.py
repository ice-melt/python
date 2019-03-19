#!/usr/bin/python3

# 地址管理器
class Urls(object):

    def __init__(self):
        """
        newUrls集合保存未爬取的url
        oldUrls集合保存已爬取的url
        """
        self.newUrls = set()
        self.oldUrls = set()

    def get_new_url(self):
        """
        从未爬取newUrls集合中拿到一个url，并将其放入到已爬取数组
        :return:
        """
        url = self.newUrls.pop()
        self.oldUrls.add(url)
        return url

    def add_new_url(self, url):
        """
        向未爬取newUrls集合中添加一项url
        :param url:
        :return:
        """
        if url not in self.newUrls and url not in self.oldUrls:
            self.newUrls.add(url)

    def add_new_urls(self, urls):
        """
        向未爬取newUrls集合中添加多项url
        :param urls:
        :return:
        """
        for url in urls:
            self.add_new_url(url)

    def get_new_urls_length(self):
        """
        获取未爬取newUrls集合大小
        :return:
        """
        return len(self.newUrls)