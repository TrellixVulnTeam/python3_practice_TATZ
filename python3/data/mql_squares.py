import  matplotlib.pyplot as plt

#创建列表
input_values = [1, 2 ,3 ,4, 5]
squares = [1, 4, 9, 16, 25]
#根据参数绘制图形
plt.plot(input_values, squares, linewidth = 5)

#设置标题，并给坐标轴加上标签
plt.title("Square Numbers",fontsize=14)
plt.xlabel("value",fontsize = 14)
plt.ylabel("square of value",fontsize = 14)
#设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14);
plt.show()