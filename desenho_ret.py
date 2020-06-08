# Desenhando retângulo sobre imagem

import cv2

imagem = cv2.imread('lena.png')
verde = (0,255,0)
#Argumentos:
#imagem, posição inicial, posição final,
#cor, espessura da linha
cv2.rectangle(imagem, (20, 20), (80, 120), verde, 5)
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)
