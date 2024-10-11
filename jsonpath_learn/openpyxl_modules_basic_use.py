# openpyxl modules basic use

from openpyxl import Workbook

wb = Workbook()  # 首先我们需要现先实例化一个工作簿对象出来

ws = wb.active  # 实现的是我们的返回一个当前已经记过的工作表，激活的步骤

ws.append([])  # 添加数据

print(ws.title)

wb.save('test.xlsx')  # 这一步就是实现的是我们的指定保存的路径
