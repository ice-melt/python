#!/usr/bin/python3
# -*- coding:utf-8 -*-
from assets import useragent
from assets.log import log
from projects.crawler_for_prodect_category.category_output.output import Output
from urllib.parse import urljoin, unquote
from lxml import etree
from tkinter import *
from tkinter import ttk
import tkinter.filedialog as filedialog
import json
import time
import queue
import requests
import threading
import traceback

Logger = log('crawler.log', level='debug').logger


class App:
    def __init__(self):
        root = Tk()
        self.root = root
        self.W = 1440
        self.H = 900
        self.w = 500
        self.h = 500
        self.X = 100
        self.Y = 100
        # global veriable key
        self.clawler_key = StringVar()
        self.text_key = StringVar()
        self.window_init()
        self.create_menu()
        self.create_content()
        self.path = './'
        self.gress_bar = None
        self.notify_queue = queue.Queue()
        # self.process_msg()
        self.root.mainloop()

    def window_init(self):
        self.root.title('Product Category Collector')
        # self.root.resizable(False, False) 调用方法会禁止根窗体改变大小
        # 以下方法用来计算并设置窗体显示时，在屏幕中心居中
        self.w, self.h = self.root.winfo_width(), self.root.winfo_height()  # get frame current width,height
        self.W, self.H = self.root.maxsize()  # get screen width and height
        self.X, self.Y = (self.W - self.w) / 2, (self.H - self.h) / 2
        self.root.geometry("+%d+%d" % (self.X, self.Y))
        # self.root.bg = 'black'

    def create_menu(self):
        menu = Menu(self.root)
        about_menu = Menu(menu, tearoff=0)
        about_menu.add_command(label='version:1.0')
        menu.add_cascade(label='关于', menu=about_menu)
        self.root['menu'] = menu

    def create_content(self):
        lf = ttk.LabelFrame(self.root, text="一键汇总:请在输入框中输入网址")
        lf.pack(fill=X, padx=15, pady=8)
        top_frame = Frame(lf)
        top_frame.pack(fill=X, expand=YES, side=TOP, padx=15, pady=8)
        ttk.Entry(top_frame, textvariable=self.clawler_key, width=50).pack(fill=X, expand=YES, side=LEFT)
        ttk.Button(top_frame, text="开始", command=self.do_crawler).pack(padx=15, fill=X, expand=YES)
        bottom_frame = Frame(lf)
        bottom_frame.pack(fill=BOTH, expand=YES, side=TOP, padx=15, pady=8)
        band = Frame(bottom_frame)
        band.pack(fill=BOTH, expand=YES, side=TOP, padx=15, pady=8)
        ttk.Label(band, textvariable=self.text_key, width=50).pack(fill=X, expand=YES, side=LEFT)

    def process_msg(self):
        self.root.after(400, self.process_msg)
        while not self.notify_queue.empty():
            try:
                msg = self.notify_queue.get()
                if msg[0] == 1:
                    self.gress_bar.quit()
            except queue.Empty:
                pass

    def execute_asyn(self):
        def scan(_queue):
            for i in range(5):
                time.sleep(1)
            _queue.put((1,))

        th = threading.Thread(target=scan, args=(self.notify_queue,))
        th.setDaemon(True)
        th.start()
        self.gress_bar.start()

    def do_crawler(self):
        if self.clawler_key.get():
            result_data = self.clawler_key.get()
            self.text_key.set('您输入的网址是 %s,正在收集数据,请稍等。。。' % result_data)
            # 去爬虫
            Scheduler().main(result_data.strip())
            # Scheduler().main('https://yolanda-cn.en.alibaba.com')
            # Scheduler().main('https://win-gene.en.alibaba.com')
            # Scheduler().main('https://ifoaming.en.alibaba.com')
            self.text_key.set('Done！')

    def open_dir(self):
        d = filedialog.Directory()
        self.path = d.show(initialdir=self.path)


class LoopRequest(object):
    def __init__(self):
        self.size = 0

    def request(self, url):
        headers = {
            'User-Agent': useragent.get_user_agent()
        }
        s = requests.session()
        try:
            r = s.request(method='get', url=url, headers=headers)
            return r
        except Exception as e:
            self.size += 1
            if self.size < 5:
                return self.request(url)
            else:
                Logger.error(' ====== crawler fail ======= \n%s' % traceback.format_exc())
                Logger.info('抓取地址失败:%s' % url)
                return {'status_code': '500'}


# 页面下载
def download(url):
    """
    下载指定url页面
    :param url:
    :return:
    """
    r = LoopRequest().request(url)
    if r.status_code == 200:
        Logger.info('正在抓取地址:%s' % url)
        Logger.info('User-Agent:%s' % r.request.headers.get('user-agent'))
        return r.content
    return '404'


# 页面解析
def parser_html(url, content, product_categories, product_subcategories):
    """
    用lxml中的etree解析通过requests返回的内容
    :param url:
    :param content:`
    :param product_categories:
    :param product_subcategories:
    :return:
    """
    html = etree.HTML(content)
    xpath = "//div[contains(@class,'module-product-list')]" \
            "//div[contains(@class,'product-info')]" \
            "//a[@class='title-link icbu-link-normal']"
    item = html.xpath(xpath)

    datas = []
    for key in item:
        datas.append({
            'categories': product_categories,
            'subcategories': product_subcategories,
            'description': key.get('title'),
            'url': urljoin(url, key.get('href'))
        })
    return datas


# 调度器
class Scheduler(object):
    def __init__(self):
        """
        初始化调度器
        """
        self.output = Output()

    def main(self, root_url):
        """
        根据入口文件，开始爬取需要的内容和urls
        :param root_url:
        :return:
        """
        # 根据主页面得到第一个类目的链接地址
        self.output.set_url(root_url)
        html = download(root_url)
        if html == '404':
            Logger.error('%s 无法解析,请联系开发人员' % root_url)
            return
        doms = etree.HTML(html).xpath("//div[@tabindex='0']//a")
        if len(doms) < 1:
            Logger.error('获取类目信息失败,无法得到类目列表,len<1')
            return
        product_categories_href = doms[0].get('href')
        url = urljoin(root_url, product_categories_href)
        # 根据得到第一个类目的链接地址,从其中找到所有类目的链接
        html = download(url)
        if html == '404':
            Logger.error('%s 无法解析,请联系开发人员' % url)
            return
        doms = etree.HTML(html).xpath("//div[@module-name='icbu-pc-productGroups']/@module-data")
        if len(doms) == 0:
            Logger.error('获取类目信息失败,无法得到类目列表,len=0')
        dom = unquote(doms[0])
        mds = json.loads(dom)['mds']
        if len(mds) == 0:
            return
        module_data = mds['moduleData']
        if len(module_data) == 0:
            return
        data = module_data['data']
        if len(data) == 0:
            return
        groups = data['groups']
        if len(groups) == 0:
            return
        for group in groups:
            product_categories = group['name']
            product_categories_href = group['url']
            children = group['children']
            if product_categories == 'All Custom Products':
                continue
            if len(children) == 0:
                self.crawler(root_url, product_categories_href, product_categories, '')
            else:
                for child in children:
                    product_subcategories = child['name']
                    product_categories_href = child['url']
                    # chi = child['children']
                    self.crawler(root_url, product_categories_href, product_categories, product_subcategories)
        self.output.to_file('EXCEL')

    def crawler(self, root_url, product_categories_href, product_categories, product_subcategories):
        """
        开始爬取需要的内容和urls,并输出保存
        :param root_url: 网站根目录
        :param product_categories_href:产品类目href
        :param product_categories:产品类目名称
        :param product_subcategories:产品子类目名称
        :return:
        """
        loop_flag = True
        i = 1
        while loop_flag:
            arr = product_categories_href.split('/')
            if len(arr) < 3:
                break
            url = '%s/%s-%d/%s' % (root_url, arr[1], i, arr[2])
            i += 1
            try:
                content = download(url)
                if content == '404':
                    Logger.error('%s 无法解析,请联系开发人员' % url)
                    loop_flag = False
                    break
                datas = parser_html(url, content, product_categories, product_subcategories)
                if len(datas) == 0:
                    loop_flag = False
                else:
                    self.output.store_datas(datas)
            except Exception as e:
                # print('e.message:\t', e.message)
                Logger.error(' ====== crawler fail ======= \n%s' % traceback.format_exc())


if __name__ == '__main__':
    app = App()
    # Scheduler().main('https://yolanda-cn.en.alibaba.com')
    # Scheduler().main('https://win-gene.en.alibaba.com')
    # Scheduler().main('https://ifoaming.en.alibaba.com')

else:
    app = App()
