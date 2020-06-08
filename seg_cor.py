# Segmentação por Cor

import cv2
import numpy as np

img = cv2.imread('lena.png')
# transforma para HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imwrite("hsv.png", hsv)
# cria um mínimo e um máximo de [H,S,V]
lower = np.array([130,0,0]) # violeta
upper = np.array([160,255,255]) # violeta
# cria uma mascara que vai conter só o intervalo criado
mask = cv2.inRange(hsv, lower, upper)
# cria uma imagem nova “res” aplicando a mascara na imagem original
res = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("mascara", mask)
cv2.imshow("res", res)
cv2.waitKey(0)
