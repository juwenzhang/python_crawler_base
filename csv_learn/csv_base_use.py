import csv

with open("text.csv", "a", encoding="utf-8", newline="") as f:
    # 首先我们是需要先实现我们的创建一个 csv 文件镀锡
    csv_f = csv.writer(f)
    csv_f.writerow(["标题", "链接"])