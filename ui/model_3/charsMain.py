
import matplotlib.pyplot as plt

y_1 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6,0.7,0.8,0.9,1]
x= [1,2,3,4,5,6,7,8,9,10]
# y_2 = [i * 4 for i in x]

print(x)
print(y_1)
# print(y_2)

# 创建画布
plt.figure()

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




