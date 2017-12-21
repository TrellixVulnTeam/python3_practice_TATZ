# scatter() 绘制散点图

import matplotlib.pyplot as plt

#x_values = [1, 2, 3, 4, 5]
#y_values = [1, 4, 9, 16,25]
#自动计算数据
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors="none",s=10)

#设置图表标题,并给坐标加上坐标
plt.title("squares numbers",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("squares of value",fontsize=14)
#设置刻度标记大小
plt.tick_params(axis="both",which="major",labelsize=10)

plt.axis([0,1100,0,1100000])

plt.savefig('squres.png',bbox_inches="tight")
plt.show()
