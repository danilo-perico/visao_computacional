# Dilatação

import cv2
import numpy as np

img = cv2.imread('j.png')
kernel = np.ones((5,5),int)
dilatacao = cv2.dilate(img,kernel,iterations = 1)
cv2.imshow("Imagem", dilatacao)
cv2.waitKey(0)
