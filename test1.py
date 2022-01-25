import os
import sys
import glob
import  cv2
from datetime import date, time, datetime, timedelta
from operator import itemgetter
from math import exp, log, sqrt
import os

# inputPath ='VOCdevkit/VOC2007/ImageSets/Segmentation'
# for input_file in glob.glob(os.path.join(inputPath,'*.txt')):
#       with open(input_file, 'r') as filereader:
#           print(filereader.name)
inputDir='VOCdevkit/VOC2007/SegmentationClass2'
for imagefile in glob.glob(inputDir+'/*.jpg'):
    img=cv2.imread(imagefile)
    imgName= imagefile.split('\\')
    imaTrueName=imgName[1].split('.')
    cv2.imwrite('VOCdevkit/VOC2007/SegmentationClass/'+imaTrueName[0]+'.png',img)

