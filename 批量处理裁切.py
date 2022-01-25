import cv2
import glob
import skimage
k = 0
# for imagefile in glob.glob(r'stone/image/phone.jpg'):
image = cv2.imread(r'img_stone/phone.jpg')
    # cv2.imshow("ceshi",mask)
print("开始了--------------------------------------------")
print(image.shape)
print(image.shape[0])	#height(rows) of mask 1920
print(image.shape[1])	#width(colums) of mask 2560
for i in range(1,15):
    print("i在执行+++++++++++++++++++++++++++++++++++++++")
    for j in  range(1,11):
        dst= image[(i-1)*256:i*256,(j-1)*256:j*256]
        print(dst.shape)
        print("j在执行-----------------------------------")
            # cv2.waitKey()
        k+=1
        cv2.imwrite(r'img_stone/phonetest/{}.jpg'.format(k), dst)
    # print(mask.shape[2])	#the pixels value is made up of three primary colors
    # for j in range(mask.shape[0]):
    #     for i in range(mask.shape[1]):
    #         dst = mask[i:i + 256, j:j + 256]  # cutting
    #         i = i + 256
    #     # cv2,imshow('mask', dst)
    #     # cv2.waitKey()
    #         cv2.imwrite('./岩石薄片/after/{}.jpg'.format(i), dst)
    # j = j + 256
    # dst = mask[0:256, 0:256]
    # print("在这呢")
    # cv2.imshow('mask', dst)
    print("到这了!")
    print("结束了!")