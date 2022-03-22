import cv2
from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity

img1 = cv2.imread('img.png')
img2 = cv2.imread('imgs/bilateral.png')

SSIM = structural_similarity(img1, img2, multichannel=True)

print('SSIM: ', SSIM)