# Muhammad Muhfi A.R
# 1217070047

import cv2
import  numpy as np
image = cv2.imread("muhfi.jpeg")
height, width = image.shape[:2]
# membuat matriks M dengan contoh Tx = 100 & Ty=50
M =np.float32([[1,0,100],[0,1,50]])
image_translasi = cv2.warpAffine(image,M,(height,width))
cv2.imshow('Citra',image)
cv2.imshow('Citra hasil translasi',image_translasi)
cv2.waitKey(0)