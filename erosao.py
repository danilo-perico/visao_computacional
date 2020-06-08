# Erosao

import cv2
import numpy as np

img = cv2.imread('j_ruido.png')
kernel = np.ones((5,5),int)
erosao = cv2. erode(img,kernel,iterations = 1)
cv2.imshow("Original", img)
cv2.imshow("Imagem", erosao)
cv2.waitKey(0)
