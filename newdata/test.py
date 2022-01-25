import  glob
import cv2
import os
k=0
for maskfile in glob.glob(r'../newdata/images/*.jpg'):

    print("21312312312")
    image_name=maskfile.split("\\")[1].split(".")[0]
    img=cv2.imread(maskfile)
    #cv2.imwrite("../newdata/pngMasks/"+image_name+".png",img)
    k+=1
    cv2.imwrite("../newdata/vimages/{}.jpg".format(k), img)