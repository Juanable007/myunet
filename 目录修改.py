import cv2
import glob, os

# path = r'E:/Massachusetts Roads Dataset/trains'
# file = glob.glob(os.path.join(path, "*.jpg"))
# # print(file)
# maskpath= r"E:/Massachusetts Roads Dataset/trains_mask"
# maskfile = glob.glob(os.path.join(maskpath, "*.jpg"))
testpath = r'E:/Massachusetts Roads Dataset/tests'
testfile = glob.glob(os.path.join(testpath,"*.jpg"))
print(testfile)
#
# # image
# k=1
# for i in file:
#     # print(i)
#     img= cv2.imread(i)
#     # 存储原图
#     dir="./dataset/train/"+str(k)+"/images/"
#     if not os.path.exists(dir):  # 如果不存在路径，则创建这个路径，关键函数就在这两行，其他可以改变
#         os.makedirs(dir)
#     cv2.imwrite(dir+str(k)+".jpg",img)
#     k=k+1
#
# # maks
# n =1
# for j in maskfile:
#     # print(j)
#     img= cv2.imread(j)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 把输入图像灰度化
#     # 直接阈值化是对输入的单通道矩阵逐像素进行阈值分割。
#     ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(4, 4))
#     opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
#     dir="./dataset/train/"+str(n)+"/masks/"
#     if not os.path.exists(dir):  # 如果不存在路径，则创建这个路径，关键函数就在这两行，其他可以改变
#         os.makedirs(dir)
#     cv2.imwrite(dir+str(n)+".jpg",opened)
#     n=n+1
#test
m =1
for k in testfile:

    img= cv2.imread(k)
    # 存储原图
    dir="./dataset/test/"+str(m)+"/images/"
    if not os.path.exists(dir):  # 如果不存在路径，则创建这个路径，关键函数就在这两行，其他可以改变
        os.makedirs(dir)
    cv2.imwrite(dir+str(m)+".jpg",img)
    m=m+1
# img= cv2.imread('mask2.jpg')
# print(img.shape)
# print(img)
# print('----')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 把输入图像灰度化
# # 直接阈值化是对输入的单通道矩阵逐像素进行阈值分割。
# ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
# print(binary.shape)
# print(binary)
# print('---')
# kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
# eroded = cv2.erode(binary,kernel1)#腐蚀

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(4, 4))
# opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
# print(opened.shape)
# print(opened)
# cv2.imshow('open',opened)
# cv2.waitKey(0)