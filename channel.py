import cv2
import glob
import numpy as np
import os


for imagefile in glob.glob('test_img\\img\\*.jpg'):
    img = cv2.imread(imagefile)
    B,G,R = cv2.split(img)
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    H,S,V = cv2.split(img1)
    image = cv2.merge([B,G,R,H])
    filename = imagefile.split('\\')[-1]
    # print(filename)
    cv2.imwrite('test_img_4\\' + filename,image)


