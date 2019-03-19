#!/usr/bin/python3
from category_output import to_csv
from category_output import to_excel
from category_output import to_html

output_map = {
    'CSV': to_csv,
    'HTML': to_excel,
    'EXCEL': to_html,
}


def factory(file_type):
    """
    输出工厂,默认生产 output html 实例对象
    :param file_type:
    :return:  根据传入的参数默认生产出对应的output实例对象
    """
    if file_type not in output_map:
        return output_map['HTML']
    else:
        return output_map[file_type]