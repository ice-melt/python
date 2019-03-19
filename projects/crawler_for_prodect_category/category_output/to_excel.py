# !/usr/bin/python3
from category_output import output_utils
import xlwt

def output(filename, datas):
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
        for i in range(len(datas)):
            key = datas[i]
            categories = key['categories'].replace('/', ' ')
            if sheet_name != categories:
                sheet_name = categories
                sheet = wbk.add_sheet(sheet_name)
                sheet.write(0, 0, 'Sequence', style)
                sheet.write(0, 1, 'Product SubCategories', style)
                sheet.col(1).width = 256 * 20
                sheet.write(0, 2, 'Description', style)
                sheet_rows += row
            row = i - sheet_rows + 1
            if row == -21:
                print(row)
            sheet.write(row, 0, row)
            sheet.write(row, 1, key['subcategories'])
            link = 'HYPERLINK("%s","%s")\n' % (key['url'], key['description'].replace('"', '""'))
            sheet.write(row, 2, xlwt.Formula(link))
        wbk.save(output_utils.get_filename(filename, 'xls'))