#!/usr/bin/python3
from category_output import output_factory
from category_output import test

class Output:
    def __init__(self, url=""):
        self.datas = []
        self.url = url
        self.file_name = url.replace('https://', '').replace('http://', '')

    def set_url(self, url):
        self.url = url
        self.file_name = url.replace('https://', '').replace('http://', '')

    def store_datas(self, datas):
        """
        将爬取的datas数据存放到self.datas中
        :param datas:
        :return:
        """
        for key in datas:
            self.datas.append(key)

    def to_file(self, file_type):
        output_factory.factory(file_type).output(self.file_name, self.datas)


if __name__ == '__main__':
    output = Output('https://baidu.com')
    test_datas = test.get_datas()
    output.store_datas(test_datas)
    output.to_file('HTML')
    output.to_file('CSV')
    output.to_file('EXCEL')