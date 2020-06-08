# Segmentação por Agrupamento - KMeans

import numpy as np
import cv2 as cv

img = cv.imread('lena.png')
Z = img.reshape((-1,3))

# converte para np.float32
Z = np.float32(Z)

# define criterio, numero de clusters(K)
criterio = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 16
# aplica kmeans
ret,label,center=cv.kmeans(Z,K,None,criterio,10,cv.KMEANS_RANDOM_CENTERS)
print(center)
# converte de volta para uint8
center = np.uint8(center)
# volta para formato da imagem
res = center[label.flatten()]
res2 = res.reshape((img.shape))
cv.imshow('res2',res2)
cv.waitKey(0)