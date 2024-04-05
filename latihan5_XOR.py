# Muhammad Muhfi A.R
# 1217070047

import cv2
import numpy as np
# membuat matriks untuk menggambar persegi
persegi = np.zeros((400,400),dtype="uint8")
cv2.rectangle(persegi,(60,60),(340,340),255,-1)
# membuat matriks lingkaran
lingkaran =np.zeros((400,400),dtype="uint8")
cv2.circle(lingkaran,(200,200),150,255,-1)

# Penggunaan AND
XOR=cv2.bitwise_xor(persegi,lingkaran)
cv2.imshow('Persegi',persegi)
cv2.imshow("lingkaran",lingkaran)
cv2.imshow("Operasi OR", XOR)
cv2.waitKey(0)