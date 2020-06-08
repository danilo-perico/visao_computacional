# Filtro da Média

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
blur = cv2.blur(img,(5,5))
plt.imsave("lena2.png", blur)