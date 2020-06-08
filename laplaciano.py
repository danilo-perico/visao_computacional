# Detector de Borda - Lapaciano

import cv2

img = cv2.imread('lena.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
laplacian = cv2.Laplacian(img,-1, ksize=3)
cv2.imwrite('lenaLaplace.png', laplacian)
cv2.waitKey(0)
