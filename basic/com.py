from openpyxl import Workbook

write_wb = Workbook()

write_ws = write_wb.create_sheet('생성시트')

write_ws = write_wb.active
write_ws['A1'] = '숫자'

write_ws.append([1,2,3,])

write_wb.save('/Users/ms/PycharmProjects/pythonGrammer/basic function/숫자.xlsx')
