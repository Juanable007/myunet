# import  numpy as np
# import cv2
# np.set_printoptions(threshold=np.inf)
# img=cv2.imread("img_stone/binaryMask/1.png")
# print(img.shape)
#
# arr=np.array(img)
# print(arr)
#
# import glob

import  numpy as np
import cv2
import os
import glob
np.set_printoptions(threshold=np.inf)
# img=cv2.imread("img_stone/image/1.jpg")
# print(img.shape)
#
# arr=np.array(img)
# print(arr)

maskdir='newdata/binaryMasks'
maskfiles =glob.glob(os.path.join(maskdir, "*.png"))
for maskfile in maskfiles:
    img = cv2.imread(maskfile, cv2.IMREAD_GRAYSCALE)
    imgName=maskfile.split("\\")[1].split('.')[0]
    # print(imgName)
    ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    th2
    imgName=imgName+".bmp"
    cv2.imwrite("newdata/testBinary/"+imgName, th2)