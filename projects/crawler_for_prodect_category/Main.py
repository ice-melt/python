#!/usr/bin/python3
# -*- coding:utf-8 -*-
import requests
import codecs
from modules import useragent
from modules import log
import json
from urllib.parse import urljoin, unquote
from lxml import etree
import pickle
import xlwt
import traceback
from tkinter import *
from tkinter import ttk
import tkinter.filedialog as filedialog
import time
import queue
import threading
import csv
Logger = log.Logger('crawler.log', level='debug').logger


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
    xpath = "//div[contains(@class,'module-product-list')]"\
            "//div[contains(@class,'product-info')]"\
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


# 序列化
def object_serialize(filename, data):
    with open('%s.pkl' % filename, 'wb') as f:
        pickle.dump(data, f)


# 反序列化
def object_unserialize(filename):
    with open('%s.pkl' % filename, 'rb') as f:
        return pickle.load(f)


# 导出数据到html
class Output(object):
    def __init__(self):
        """
        定义需要爬取的内容的数组
        """
        self.datas = []
        self.filename = 'product.temp'

    def get_filename(self, suffix):
        prefix = self.filename.replace('https://', '').replace('http://', '')
        timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        self.filename = '%s_%s.%s' % (prefix, timestamp, suffix)
        return self.filename

    def store_datas(self, datas):
        """
        将爬取的datas数据存放到self.datas中
        :param datas:
        :return:
        """
        for key in datas:
            self.datas.append(key)

    def output_html(self):
        """
        将爬取的数据导出到html
        :return:
        """
        Logger.info('Output to html file, please wait ...')
        # object_serialize('object.pkl',self.datas)
        # categories , description,url
        with codecs.open(self.get_filename('html'), 'w', 'utf-8') as file:
            file.write('<html>\n')
            file.write('<head>\n')
            file.write('<meta charset="utf-8"/>\n')
            file.write('<style>\n')
            file.write('table{font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;'
                       'width:100%;border-collapse:collapse;}\n')
            file.write('table th,table td{font-size:1em;border:1px solid #98bf21;padding:3px 7px 2px 7px;}\n')
            file.write('table th{font-size:1.1em;background-color:#A7C942;color:#ffffff;'
                       'padding:5px 7px 4px 7px;text-align:left;}\n')
            file.write('table tr.alt td{background-color:#EAF2D3;color:#000000;}\n')
            file.write('a:link{text-decoration: none;}\n')
            file.write('a:visited{text-decoration: none;}\n')
            file.write('a:hover{text-decoration: underline;}\n')
            file.write('</style>\n')
            file.write('</head>\n')
            file.write('<body>\n')
            file.write('<table>\n')
            # 输出首行
            file.write('<tr><th>Sequence</th><th>Product Categories</th>'
                       '<th>Product SubCategories</th><th>Description</th></tr>\n')
            for i in range(len(self.datas)):
                key = self.datas[i]
                clazz = '' if i % 2 == 0 else ' class="alt" '
                file.write('<tr %s><td>%05d</td><td>%s</td><td>%s</td>'
                           '<td><a target="_blank" href="%s">%s</a></td></tr>\n'
                           % (clazz, i+1, key['categories'], key['subcategories'], key['url'], key['description']))
            file.write('</table>\n')
            file.write('</body>\n')
            file.write('</html>\n')
        Logger.info(' Save completed !')

    def output_csv(self):
        """
        将爬取的数据导出到html
        :return:
        """
        Logger.info('Output to csv file, please wait ...')
        # categories , description,url
        with open(self.get_filename('csv'), 'w') as csvfile:
            file = csv.writer(csvfile)
            # 写入首行
            file.writerow(['Sequence', 'Product Categories', 'Product SubCategories', 'Description', 'URL'])
            for i in range(len(self.datas)):
                key = self.datas[i]
                sequence = i+1
                categories = key['categories']
                subcategories = key['subcategories']
                description = key['description']
                url = key['url']
                file.writerow([sequence, categories, subcategories, description, url])
        Logger.info(' Save completed !')

    def output_excel(self):
        wbk = xlwt.Workbook(encoding='utf-8')
        pattern = xlwt.Pattern()
        # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        # May be: 8 through 63.
        # 0 = Black, 1=White, 2=Red, 3=Green, 4=Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan,
        # 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown),
        # 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
        pattern.pattern_fore_colour = 5
        borders = xlwt.Borders()
        # DASHED虚线 NO_LINE没有 THIN实线
        borders.left = xlwt.Borders.THIN
        # May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR,
        # MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED,
        # MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
        borders.right = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN
        borders.left_colour = 0x40
        borders.right_colour = 0x40
        borders.top_colour = 0x40
        borders.bottom_colour = 0x40
        style = xlwt.XFStyle()
        style.pattern = pattern
        style.borders = borders
        sheet_name = ''
        sheet_rows = 0
        row = 0
        sheet = None
        for i in range(len(self.datas)):
            key = self.datas[i]
            categories = key['categories'].replace('/', ' ')
            if sheet_name != categories:
                sheet_name = categories
                sheet = wbk.add_sheet(sheet_name)
                sheet.write(0, 0, 'Sequence', style)
                sheet.write(0, 1, 'Product SubCategories', style)
                sheet.col(1).width = 256*20
                sheet.write(0, 2, 'Description', style)
                sheet_rows += row
            row = i-sheet_rows+1
            if row == -21:
                print(row)
            sheet.write(row, 0, row)
            sheet.write(row, 1, key['subcategories'])
            link = 'HYPERLINK("%s","%s")\n' % (key['url'], key['description'].replace('"', '""'))
            sheet.write(row, 2, xlwt.Formula(link))
        wbk.save(self.get_filename('xls'))


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
        self.output.filename = root_url
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
        self.output.output_excel()
        # self.output.output_html()
        # self.output.outputCSV()

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