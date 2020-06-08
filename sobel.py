# Detector de Borda - Sobel

import cv2

img = cv2.imread('lena.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sobelX = cv2.Sobel(img, -1, 1, 0)
sobelY = cv2.Sobel(img, -1, 0, 1)
cv2.imwrite('lenaX.png', sobelX)
cv2.imwrite('lenaY.png', sobelY)
cv2.waitKey(0)
