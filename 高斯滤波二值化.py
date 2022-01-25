import  cv2
import os
# 读取灰度图
img = cv2.imread(os.path.join(os.path.dirname(
                                    os.path.abspath(__file__)),r'data/label.png'), 0)

# 全局阈值
ret1, th_img1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Otsu’s 二值化
re2, th_img2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Otsu’s 二值化之前先对图像进行高斯滤波处理，平滑图像，去除噪声
# （5,5）为高斯核大小，0为标准差
blur = cv2.GaussianBlur(img, (5, 5), 0)
re3, th_img3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


cv2.imwrite("newdata/imgs/"+"Original.png", img)
cv2.imwrite("newdata/imgs/"+"OriginalNoiseImage.png", th_img1)
cv2.imwrite("newdata/imgs/"+"OTSU.png", th_img2)
cv2.imwrite("newdata/imgs/"+"GaussianfilteredOTSU.png", th_img3)

cv2.imshow("Original Noise Image", img)
cv2.imshow("globe threshhold", th_img1)
cv2.imshow("OTSU", th_img2)
cv2.imshow("Gaussian filtered OTSU", th_img3)

cv2.waitKey(0)
cv2.destroyAllWindows()