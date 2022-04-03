
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

y = np.array([35, 65])

plt.pie(y,
        labels=['Rock','Pore'], # 设置饼图标签
        colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"], # 设置饼图颜色
        explode=(0, 0.03),  # 第二部分突出显示，值越大，距离中心越远
        autopct='%.2f%%',  # 格式化输出百分比
       )

plt.title("岩石颗粒孔隙度占比饼状图") # 设置标题
plt.show()
plt.savefig('pie.png')

y_1 = [0.3430, 0.3740, 0.39, 0.40, 0.43, 0.45, 0.4275, 0.4103, 0.3821, 0.3907]
x= ['500μm.png', 'img0.png', 'img.png', 'img1.png', 'img2.png', 'img3.png', 'img4.png', 'img5.png', 'img6.png', 'img7.png']
# y_2 = [i * 4 for i in x]

print(x)
print(y_1)
# print(y_2)

# 创建画布
plt.figure()
# my_y_ticks = np.arange(0.0, 1, 100)
# plt.yticks(my_y_ticks)
plt.ylim(0.3,0.6)

# plt.ylim(1,10)

'''绘制第一条数据线
1、节点为圆圈
2、线颜色为红色
3、标签名字为y1-data
'''
plt.plot(x, y_1, marker='o', color='r', label='y1-data')

'''绘制第二条数据线
1、节点为五角星
2、线颜色为蓝色
3、标签名字为y2-data
'''
# plt.plot(x, y_2, marker='*', color='b', label='y2-data')

# 显示图例（使绘制生效）
plt.legend()

# 横坐标名称
plt.xlabel('x_label')

# 纵坐标名称
plt.ylabel('y_label')

# 保存图片到本地
plt.savefig('pci.png')

# 显示图片
plt.show()




