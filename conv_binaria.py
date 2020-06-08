# Conversão para Binária (preta e branca)

import cv2

imagem = cv2.imread('lena.png')
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
limiar = 127
binaria = cv2.threshold(cinza, limiar, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('binaria.png', binaria)
cv2.waitKey(0)

