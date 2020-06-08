# Filtro Gaussiano

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
median = cv2.GaussianBlur(img,(5,5),0)
plt.imsave("lena2.png", median)
