import cv2;
import numpy as np;

# Read image
im_in = cv2.imread("63.jpg", cv2.IMREAD_GRAYSCALE);

# Threshold.
# Set values equal to or above 220 to 0.
# Set values below 220 to 255.

th, im_th = cv2.threshold(im_in, 30, 255, cv2.THRESH_BINARY_INV);

# Copy the thresholded image.
im_floodfill = im_th.copy()

# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)

# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, mask, (0,0), 255);

# Invert floodfilled image
im_floodfill_inv = cv2.bitwise_not(im_floodfill)

# Combine the two images to get the foreground.
im_out = im_th | im_floodfill_inv

# Display images.
cv2.imwrite("Thresholded Image.png", im_th)
cv2.imwrite("漫水填充.png", im_floodfill)
cv2.imwrite("漫水填充图像取反.png", im_floodfill_inv)
cv2.imwrite("反图像与二值图求并集.png", im_out)

cv2.waitKey(0)
print("success")