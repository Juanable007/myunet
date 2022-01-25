
import numpy as np
import cv2


def getVarianceMean(scr, winSize):
    if scr is None or winSize is None:
        print("The input parameters of getVarianceMean Function error")
        return -1

    if winSize % 2 == 0:
        print("The window size should be singular")
        return -1

    copyBorder_map = cv2.copyMakeBorder(scr, winSize // 2, winSize // 2, winSize // 2, winSize // 2,
                                        cv2.BORDER_REPLICATE)
    shape = np.shape(scr)

    local_mean = np.zeros_like(scr)
    local_std = np.zeros_like(scr)

    for i in range(shape[0]):
        for j in range(shape[1]):
            temp = copyBorder_map[i:i + winSize, j:j + winSize]
            local_mean[i, j], local_std[i, j] = cv2.meanStdDev(temp)
            if local_std[i, j] <= 0:
                local_std[i, j] = 1e-8

    return local_mean, local_std


def adaptContrastEnhancement(scr, winSize, maxCg):
    if scr is None or winSize is None or maxCg is None:
        print("The input parameters of ACE Function error")
        return -1

    YUV_img = cv2.cvtColor(scr, cv2.COLOR_BGR2YUV)  ##转换通道
    Y_Channel = YUV_img[:, :, 0]
    shape = np.shape(Y_Channel)

    meansGlobal = cv2.mean(Y_Channel)[0]

    ##这里提供使用boxfilter 计算局部均质和方差的方法
    #    localMean_map=cv2.boxFilter(Y_Channel,-1,(winSize,winSize),normalize=True)
    #    localVar_map=cv2.boxFilter(np.multiply(Y_Channel,Y_Channel),-1,(winSize,winSize),normalize=True)-np.multiply(localMean_map,localMean_map)
    #    greater_Zero=localVar_map>0
    #    localVar_map=localVar_map*greater_Zero+1e-8
    #    localStd_map = np.sqrt(localVar_map)

    localMean_map, localStd_map = getVarianceMean(Y_Channel, winSize)

    for i in range(shape[0]):
        for j in range(shape[1]):

            cg = 0.2 * meansGlobal / localStd_map[i, j];
            if cg > maxCg:
                cg = maxCg
            elif cg < 1:
                cg = 1

            temp = Y_Channel[i, j].astype(float)
            temp = max(0, min(localMean_map[i, j] + cg * (temp - localMean_map[i, j]), 255))

            #            Y_Channel[i,j]=max(0,min(localMean_map[i,j]+cg*(Y_Channel[i,j]-localMean_map[i,j]),255))
            Y_Channel[i, j] = temp

    YUV_img[:, :, 0] = Y_Channel

    dst = cv2.cvtColor(YUV_img, cv2.COLOR_YUV2BGR)

    return dst


def main():
    img = cv2.imread(input_fn)

    if img is None:
        print("The file name error,please check it")
        return -1

    print(np.shape(img))
    dstimg = adaptContrastEnhancement(img, 15, 10)

    cv2.imwrite('output.jpg', dstimg)
    cv2.waitKey(0)

    return 0


input_fn = '../data/img(1).png'
if __name__ == '__main__':
    main()



