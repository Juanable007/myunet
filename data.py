from PIL import Image
import matplotlib.pyplot as plt
from PIL import ImageEnhance,ImageChops
import os
import cv2
import numpy as np
import skimage
from skimage import io,transform

def move(root_path,img_name,off): #平移，平移尺度为off
    img = Image.open(os.path.join(root_path, img_name))
    offset = img.offset(off,0)
    return offset

def flip(root_path,img_name):   #翻转图像
    img = Image.open(os.path.join(root_path, img_name))
    filp_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    # filp_img.save(os.path.join(root_path,img_name.split('.')[0] + '_flip.jpg'))
    return filp_img
# img = Image.open('img/0_json/img.png')
# label = Image.open('img/0_json/label.png')
# flip_img = ImageChops.offset(img,35)
# flip_label = ImageChops.offset(label,35)
# flip_img.save('img/0_json/img_offset.png')
# flip_label.save('img/0_json/label_offset.png')


def rotation(root_path, img_name):
    angle = np.random.uniform(-180,180)
    img = Image.open(os.path.join(root_path, img_name))
    rotation_img = img.rotate(angle) #旋转角度
    # rotation_img.save(os.path.join(root_path,img_name.split('.')[0] + '_rotation.jpg'))
    return rotation_img


def randomColor(root_path, img_name): #随机颜色
    """
    对图像进行颜色抖动
    :param image: PIL的图像image
    :return: 有颜色色差的图像image
    """
    image = Image.open(os.path.join(root_path, img_name))
    random_factor = np.random.randint(0, 31) / 10.  # 随机因子
    color_image = ImageEnhance.Color(image).enhance(random_factor)  # 调整图像的饱和度
    random_factor = np.random.randint(10, 21) / 10.  # 随机因子
    brightness_image = ImageEnhance.Brightness(color_image).enhance(random_factor)  # 调整图像的亮度
    random_factor = np.random.randint(10, 21) / 10.  # 随机因子
    contrast_image = ImageEnhance.Contrast(brightness_image).enhance(random_factor)  # 调整图像对比度
    random_factor = np.random.randint(0, 31) / 10.  # 随机因子
    return ImageEnhance.Sharpness(contrast_image).enhance(random_factor)  # 调整图像锐度


def contrastEnhancement(root_path,img_name):#对比度增强
    image = Image.open(os.path.join(root_path, img_name))
    enh_con = ImageEnhance.Contrast(image)
    contrast = 1.5
    image_contrasted = enh_con.enhance(contrast)
    return image_contrasted

def brightnessEnhancement(root_path,img_name):#亮度增强
    image = Image.open(os.path.join(root_path, img_name))
    enh_bri = ImageEnhance.Brightness(image)
    brightness = 1.5
    image_brightened = enh_bri.enhance(brightness)
    return image_brightened

def colorEnhancement(root_path,img_name):#颜色增强
    image = Image.open(os.path.join(root_path, img_name))
    enh_col = ImageEnhance.Color(image)
    color = 1.5
    image_colored = enh_col.enhance(color)
    return image_colored

#放大图像
def enlarge_img(root_path,img_name):
    img = cv2.imread(os.path.join(root_path,img_name))
    # height,width = img.shape[:2]
    fx = 1.6
    fy = 1.2
    enlarge = cv2.resize(img,(0,0),fx=fx,fy=fy,interpolation=cv2.INTER_CUBIC)
    return enlarge

#缩小图像
def shrink_img(root_path,img_name):
    img = cv2.imread(os.path.join(root_path,img_name))
    height,width = img.shape[:2]
    size = (int(width*0.3),int(height*0.5))
    shrik = cv2.resize(img,size,interpolation=cv2.INTER_AREA)
    return shrik

#缩放比例
def scale_img(root_path,img_name):
    # Scikit Image. 'img' = Input Image, 'scale' = Scale factor
    # For details about 'mode', checkout the interpolation section below.
    scale_out = skimage.transform.rescale(img, scale=2.0, mode='constant')
    scale_in = skimage.transform.rescale(img, scale=0.5, mode='constant')
    # Don't forget to crop the images back to the original size (for
    # scale_out)



# img = cv2.imread('img/0_json/img.png')
# label = cv2.imread('img/0_json/label.png')
# height,width = img.shape[:2]
# size = (int(width*0.7),int(height*0.7))
# shrik = cv2.resize(img,size,interpolation=cv2.INTER_AREA)

# fx = 1.1
# fy = 1.2
# enlarge = cv2.resize(img,(0,0),fx=fx,fy=fy,interpolation=cv2.INTER_CUBIC)
# enlarge_label = cv2.resize(label,(0,0),fx=fx,fy=fy,interpolation=cv2.INTER_CUBIC)
# cv2.imwrite('img/0_json/label_enlatge.png',enlarge_label)
# cv2.imwrite('img/0_json/img_enlatge.png',enlarge)


#
from PIL import Image
from PIL import ImageEnhance
import os
import cv2
import numpy as np
img_path = 'dataset/JPEGImages/'
label_path = 'dataset/SegmentationClassPNG/'
j= 11514
for i in range(4935,6579):
    name = str(i) + '.jpg'
    save_name = str(j) + '.jpg'
    img = Image.open(os.path.join(img_path,name))
    filp_img = img.rotate(270)
    filp_img.save(os.path.join(img_path,save_name))
    label = Image.open(os.path.join(label_path,name))
    flip_label = label.rotate(270)
    flip_label.save(os.path.join(label_path,save_name))
    j = j+1



