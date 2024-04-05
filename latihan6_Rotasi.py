# Muhammad Muhfi A.R
# 1217070047

import cv2
import  numpy as np
image = cv2.imread("muhfi.jpeg")

(height,width)=image.shape[0:2]
rotasimatriks = cv2.getRotationMatrix2D((width/2,height/2),-90,0.5)
rotasicitra = cv2.warpAffine(image,rotasimatriks,(width,height))
cv2.imshow('Citra Rotasi',rotasicitra)
cv2.waitKey(0)