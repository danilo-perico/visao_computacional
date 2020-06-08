# Flip Horizontal

import cv2

imagem = cv2.imread('lena.png')
flip_horizontal = imagem[::-1,:]
cv2.imshow("Flip Horizontal", flip_horizontal)
cv2.waitKey(0)
