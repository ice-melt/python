#!/usr/bin/python3
from projects.crawler_for_prodect_category.category_output import output_utils
import codecs

Logger = output_utils.Logger


def output(filename, datas):
    """
    将爬取的数据导出到html
    :return:
    """
    Logger.info('Output to html file, please wait ...')
    # object_serialize('object.pkl',self.datas)
    # categories , description,url
    with codecs.open(output_utils.get_filename(filename, 'html'), 'w', 'utf-8') as file:
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
        for i in range(len(datas)):
            key = datas[i]
            clazz = '' if i % 2 == 0 else ' class="alt" '
            file.write('<tr %s><td>%05d</td><td>%s</td><td>%s</td>'
                       '<td><a target="_blank" href="%s">%s</a></td></tr>\n'
                       % (clazz, i + 1, key['categories'], key['subcategories'], key['url'], key['description']))
        file.write('</table>\n')
        file.write('</body>\n')
        file.write('</html>\n')
    Logger.info(' Save completed !')
