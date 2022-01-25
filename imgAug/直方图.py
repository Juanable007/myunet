#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:Sui yue
@describe: 灰度直方图，描述每个灰度级在图像矩阵中的像素个数或者占有率
@time: 2019/09/15
"""

import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

#对于8位图，图像的灰度级范围式0~255之间的整数，通过定义函数来计算直方图
def calcGrayHist(image):
 #灰度图像矩阵的高、宽
 rows, cols = image.shape
 #存储灰度直方图
 grayHist=np.zeros([256],np.uint64)
 for r in range(rows):
  for c in range(cols):
   grayHist[image[r][c]] +=1
 return grayHist
#主函数
if __name__=="__main__":
 #第一个参数式图片地址，你只需放上你的图片就可
 image = cv2.imread('../data/img(1).png', cv2.IMREAD_GRAYSCALE)
 cv2.imshow("image", image)
 print("Usge:python histogram.py imageFile")
 #计算灰度直方图
 grayHist=calcGrayHist(image)
 #画出灰度直方图
 x_range=range(256)
 plt.plot(x_range,grayHist,'r',linewidth=2,c='black')
 #设置坐标轴的范围
 y_maxValue=np.max(grayHist)
 plt.axis([0,255,0,y_maxValue])
 plt.ylabel('gray level')
 plt.ylabel("number or pixels")
 # 显示灰度直方图
 plt.show()
 cv2.waitKeyEx(0)