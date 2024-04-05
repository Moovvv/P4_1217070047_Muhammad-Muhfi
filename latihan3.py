# Muhammad Muhfi A.R
# 1217070047

import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('muhfi.jpeg')
img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]
img_type = img.dtype
# melakukan penambahan brigthness
img_brightness = np.zeros(img.shape, dtype=np.uint8)
def brighter(nilai):
    for y in range(0,img_height):
        for x in range (0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue))/3
            gray += nilai
            if gray > 255:
                gray= 255
            if gray < 0:
                gray = 0
            img_brightness[y][x] = (gray,gray,gray)

brighter(-100)
plt.imshow(img_brightness)
plt.title('Brightness -100')
plt.show()

brighter(100)
plt.imshow(img_brightness)
plt.title('Brightness 100')
plt.show()


