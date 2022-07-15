import xlrd
book = xlrd.open_workbook('resources/file_example_XLS_10.xls')
print(book.nsheets)
print(book.sheet_names())
sheet = book.sheet_by_index(0)
print(f'Количество столбцов {sheet.ncols}')
print(f'Количество строк {sheet.nrows}')
print(f'Ячейка 9:1 = {sheet.cell_value(rowx=9, colx=1)}')
for rx in range(sheet.nrows):
    print(sheet.row(rx))