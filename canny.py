# Detector de Borda - Canny

import cv2

img = cv2.imread('lena.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#imagem de entrada, threshold_baixo, threshold_alto
edges = cv2.Canny(img,100,200)
cv2.imwrite('lenaCanny.png', edges)
cv2.waitKey(0)
