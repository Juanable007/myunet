import cv2
import glob
import numpy as np
import os



# k = 0
#图像分割 512*512
# for imagefile in glob.glob('E:\\Massachusetts Roads Dataset\\tiff\\train\\*.tiff'):
#     image = cv2.imread(imagefile)
#     for i in range(1,4):
#         for j in range(1,4):
#             if i == 1 and j == 1:
#                 dst = image[(i-1)*512:i*512,(j-1)*512:j*512]
#             elif i == 1 and j != 1:
#                 dst = image[(i-1)*512:i*512,(j-1)*512-18:j*512-18]
#             elif j == 1 and i != 1:
#                 dst = image[(i-1)*512-18:i*512-18,(j-1)*512:j*512]
#             else:
#                 dst = image[(i-1)*512-18:i*512-18,(j-1)*512-18:j*512-18]
#             k+=1
#             cv2.imwrite('VOCdevkit/VOC2007/JPEGImages/{}.jpg'.format(k), dst)
#标签分割 512*512
# for imagefile in glob.glob('E:\\Massachusetts Roads Dataset\\tiff\\train_labels\\*.tif'):
#     image = cv2.imread(imagefile)
#     for i in range(1,4):
#         for j in range(1,4):
#             if i == 1 and j == 1:
#                 dst = image[(i-1)*512:i*512,(j-1)*512:j*512]
#             elif i == 1 and j != 1:
#                 dst = image[(i-1)*512:i*512,(j-1)*512-18:j*512-18]
#             elif j == 1 and i != 1:
#                 dst = image[(i-1)*512-18:i*512-18,(j-1)*512:j*512]
#             else:
#                 dst = image[(i-1)*512-18:i*512-18,(j-1)*512-18:j*512-18]
#             k+=1
#             cv2.imwrite('VOCdevkit/VOC2007/SegmentationClass/{}.jpg'.format(k), dst)
# for imagefile in glob.glob('G:\\Datasets\\deepglobe-road-dataset\\train\\*.png'):
#     image = cv2.imread(imagefile)
#     for i in range(1,3):
#             for j in range(1,3):
#                 dst = image[(i-1)*512:i*512,(j-1)*512:j*512]
#                 cv2.imwrite('VOCdevkit/VOC2007/SegmentationClass/{}.png'.format(k), dst)
#                 k += 1
# k = 0
# #筛选黑色标签
# maskpath='SegmentationClass'
# for imagefile in glob.glob(maskpath+'/*.png'):
#     img1 = cv2.imread('0.png')
#     img = cv2.imread(imagefile)
#     difference = cv2.subtract(img,img1)
#     result = not np.any(difference)
#     if result == True:#说明是黑色的
#         os.remove(imagefile)
#         filename=imagefile.split('\\')
#         delfilename= filename[1].split('.')
#         os.remove('JPEGImages'+'/'+delfilename[0]+'.jpg')
#     continue


# img1 = cv2.imread('0.png')
# img = cv2.imread('VOCdevkit/VOC2007/SegmentationClass/0.png')
# difference = cv2.subtract(img,img1)
# result = not np.any(difference)
# print(result)

maskdir='./miou_pr_dir_route_2'
maskfiles =glob.glob(os.path.join(maskdir, "*.png"))
for maskfile in maskfiles:
    img = cv2.imread(maskfile, cv2.IMREAD_GRAYSCALE)
    imgName=maskfile.split("\\")[1]
    # print(imgName)
    ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite("miou_pr_dir/"+imgName, th2)
# for imagefile in glob.glob('test_img_route\\img\\*.jpg'):
#     img = cv2.imread(imagefile)
#     img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#     (h,s,v) = cv2.split(img)
#     img_s = cv2.equalizeHist(s)
#     kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)
#     dst = cv2.filter2D(img_s,-1,kernel=kernel)
#     img_final = cv2.merge((h,dst,v))
#     img_final = cv2.cvtColor(img_final,cv2.COLOR_HSV2BGR)
#     file = imagefile.split('\\')[-1]
#     cv2.imwrite('test_img_route\\img\\' + file,img_final)