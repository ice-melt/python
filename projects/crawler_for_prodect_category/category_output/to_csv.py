# !/usr/bin/python3
from projects.crawler_for_prodect_category.category_output import output_utils
import csv

Logger = output_utils.Logger


def output(filename, datas):
    """
     将爬取的数据导出到html
     :return:
     """
    Logger.info('Output to csv file, please wait ...')
    # categories , description,url
    with open(output_utils.get_filename(filename, 'csv'), 'w') as csvfile:
        file = csv.writer(csvfile)
        # 写入首行
        file.writerow(['Sequence', 'Product Categories', 'Product SubCategories', 'Description', 'URL'])
        for i in range(len(datas)):
            key = datas[i]
            sequence = i + 1
            categories = key['categories']
            subcategories = key['subcategories']
            description = key['description']
            url = key['url']
            file.writerow([sequence, categories, subcategories, description, url])
    Logger.info(' Save completed !')
