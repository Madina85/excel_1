from flask import Flask, render_template
from openpyxl import Workbook
excel = Workbook()

app = Flask(__name__)

@app.route('/')
def homepage():
    f = open('goods.xlsx', 'r+', encoding='utf-8')
    txt = f.readlines()
    return render_template(goods=txt)
page = excel.active
page["A1"]= "Сотрудник"
page["A2"] = "Bill"
page["A3"] = "Steve"
page["A4"] = "Elon"
page["A5"] = "Mark"

page["B1"]= "Янв"
page["B2"] = 44
page["B3"] = 10
page["B4"] = 0
page["B5"] = 78

page["C1"]= "Фев"
page["C2"] = 32
page["C3"] = 95
page["C4"] = 150
page["C5"] = 67

page["D1"]= "Март"
page["D2"] = 56
page["D3"] = 74
page["D4"] = 175
page["D5"] = 86
excel.save('goods.xlsx')    