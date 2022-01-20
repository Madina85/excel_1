from openpyxl import load_workbook

excel = load_workbook('goods.xlsx')

page = excel["Sheet"]

page['E1'] = 'Итого'
page['F1'] = 'Среднее'
page['A6'] = 'Итого'



s = page['B2'].value + page['C2'].value + page['D2'].value
sum = s
page['E2'] = sum
medium = sum / 3
page["F2"] = medium

s = page['B3'].value + page['C3'].value + page['D3'].value
sum = s
page['E3'] = sum
medium = sum / 3
page["F3"] = medium


s = page['B4'].value + page['C4'].value + page['D4'].value
sum = s
page['E4'] = sum
medium = sum / 3
page["F4"] = medium


s = page['B5'].value + page['C5'].value + page['D5'].value
sum = s
page['E5'] = sum
medium = sum / 3
page["F5"] = medium



s = page['B2'].value + page['B3'].value + page['B4'].value
sum = s
page['B6'] = sum


s = page['C2'].value + page['C3'].value + page['C4'].value
sum = s
page['C6'] = sum

s = page['D2'].value + page['D3'].value + page['D4'].value
sum = s
page['D6'] = sum

s = page['E2'].value + page['E3'].value + page['E4'].value
sum = s
page['E6'] = sum

s = page['F2'].value + page['F3'].value + page['F4'].value
sum = s
page['F6'] = sum

excel.save('goods.xlsx')