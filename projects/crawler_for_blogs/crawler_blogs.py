#!/usr/bin/python3
from modules.crawler import download
from modules.crawler import urls
import codecs
from urllib.parse import urljoin
from lxml import etree

# 页面解析
class Parser(object):

    def __init(self):
        pass

    def parser_html(self, url, content):
        """
        用lxml中的etree解析通过requests返回的内容
        :param url:
        :param content:
        :return:
        """
        html = etree.HTML(content)
        datas = self.get_datas(url, html)
        links = self.get_urls(url, html)
        return links, datas

    @staticmethod
    def get_datas(url, html):
        """
        解析需要爬取的内容
        :param url:
        :param html:
        :return:
        """
        datas = []

        data1 = html.xpath("//article[contains(@class, 'recent-post-item')]//h2")
        data2 = html.xpath("//article[contains(@class, 'recent-post-item')]//a[@class='title']")
        if len(data1) != len(data2):
            print('something error')
        else:
            for i in range(len(data1)):
                item1 = data1[i].text
                item2 = urljoin(url, data2[i].get('href'))
                print(item1)
                print(item2)
                datas.append({
                    'title': item1,
                    'url': item2
                })

        return datas

    @staticmethod
    def get_urls(url, html):
        """
        解析需要继续爬取的urls
        :param url:
        :param html:
        :return:
        """
        return [urljoin(url, key) for key in html.xpath("//nav[@class='page-nav text-center']//a[contains(@class, 'page-number')]//@href")]

# 导出数据到html
class Output(object):

    def __init__(self):
        """
        定义需要爬取的内容的数组
        """
        self.datas = []

    def store_datas(self, datas):
        """
        将爬取的datas数据存放到self.datas中
        :param datas:
        :return:
        """
        for key in datas:
            self.datas.append(key)

    def to_html(self):
        """
        将爬取的数据导出到html
        :return:
        """
        with codecs.open('data.html', 'w', 'utf-8') as file:
            file.write('<meta charset="utf-8"/>')
            for key in self.datas:
                file.write('<p><a target="_blank" href="%s">%s</a>,%s</p>\n' % (key['url'], key['title'], key['url']))

# 调度器
class Scheduler(object):

    def __init__(self):
        """
        初始化调度器
        """
        self.urls = urls.Urls()
        self.parserHTML = Parser()
        self.output = Output()

    def crawler(self, root_url):
        """
        根据入口文件，开始爬取需要的内容和urls
        :param root_url:
        :return:
        """
        self.urls.add_new_url(root_url)
        while self.urls.get_new_urls_length() > 0:
            try:
                url = self.urls.get_new_url()
                content = download.download(url)
                links, datas = self.parserHTML.parser_html(url, content)
                self.urls.add_new_urls(links)
                self.output.store_datas(datas)
            except Exception as e:
                print('crawler fail')
        self.output.to_html()


# 实例化
crawler = Scheduler()
crawler.crawler('http://www.dongwm.com/')