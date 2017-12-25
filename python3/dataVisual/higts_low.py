import csv
from matplotlib import  pyplot as plt

filename = "../source/sitka_weather_date.cvs"

with open(filename) as fo:
    reader = csv.reader(fo)
    header_row = next(reader)
     # 获取每个元素的索引,值
    for index, column_header in enumerate(header_row):
        print(index,column_header)

    highs = []
    for row in reader:
        #int 字符串转数字
        high = int(row[1])
        highs.append(high)
    print(highs)
#根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(highs, c='red')

#设置图形的格式
plt.title("Daily high temperatures", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("temperature(F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()