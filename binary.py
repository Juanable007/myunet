
import cv2

img = cv2.imread("ui/model_2/temp/joinOut/锐化.png", cv2.IMREAD_GRAYSCALE)

row = img.shape[0]
clo = img.shape[1]
k=0
for j in range(2560):
    for i in range(1920):
        if(img[i,j]>127):
            k+=1
sum= clo*row
print()

print(k)

print(k/sum)