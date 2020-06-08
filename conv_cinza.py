# Conversão para Escala de Cinza - Monocromática

import cv2

imagem = cv2.imread('lena.png')
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imwrite('cinza.png', cinza)
cv2.waitKey(0)

