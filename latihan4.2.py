# Muhammad Muhfi A.R
# 1217070047

import cv2
# membaca dua gambar
gambar1 = cv2.imread('muhfi.jpeg')
gambar2= cv2.imread('mupi.jpg')

tinggi, lebar, _= gambar1.shape
gambar2 = cv2.resize(gambar2,(lebar,tinggi))

tinggi, lebar, _= gambar1.shape
gambar2 = cv2.resize(gambar2,(lebar,tinggi))

hasil_penjumlahan = gambar1.copy()

for y in range(tinggi):
    for x in range(lebar):
        for c in range(3):
            nilai_baru = gambar1[y,x,c] + gambar2[y,x,c]
            hasil_penjumlahan[y,x,c]= min(nilai_baru,255)

cv2.imshow('Hasil penjumlahan', hasil_penjumlahan)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('hasil_penjumlahan_manual_rumus.jpg',hasil_penjumlahan)