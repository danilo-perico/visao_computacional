# Flip Vertical

import cv2

imagem = cv2.imread('lena.png')
flip_vert = imagem[:,::-1]
cv2.imshow("Flip Vertical", flip_vert)
cv2.waitKey(0)
