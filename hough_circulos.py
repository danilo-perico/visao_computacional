# Transformada de Hough - Circulos

import cv2
import numpy as np

img = cv2.imread('doces.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
# cv2.HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]])
# Parameters:	
# image – 8-bit, single-channel, grayscale input image.
# circles – Output vector of found circles. Each vector is encoded as a 3-element floating-point vector (x, y, radius) .
# circle_storage – In C function this is a memory storage that will contain the output sequence of found circles.
# method – Detection method to use. Currently, the only implemented method is CV_HOUGH_GRADIENT , which is basically 21HT , described in [Yuen90].
# dp – Inverse ratio of the accumulator resolution to the image resolution. For example, if dp=1 , the accumulator has the same resolution as the input image. If dp=2 , the accumulator has half as big width and height.
# minDist – Minimum distance between the centers of the detected circles. If the parameter is too small, multiple neighbor circles may be falsely detected in addition to a true one. If it is too large, some circles may be missed.
# param1 – First method-specific parameter. In case of CV_HOUGH_GRADIENT , it is the higher threshold of the two passed to the Canny() edge detector (the lower one is twice smaller).
# param2 – Second method-specific parameter. In case of CV_HOUGH_GRADIENT , it is the accumulator threshold for the circle centers at the detection stage. The smaller it is, the more false circles may be detected. Circles, corresponding to the larger accumulator values, will be returned first.
# minRadius – Minimum circle radius.
# maxRadius – Maximum circle radius.
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 10, param1=100, param2=30, minRadius=1, maxRadius=30)
circles = np.uint16(np.around(circles))

for i in circles[0, :]:
    center = (i[0], i[1])
    # centro circulo
    cv2.circle(img, center, 1, (255, 255, 0), 3)
    # raio circulo
    radius = i[2]
    cv2.circle(img, center, radius, (255, 0, 255), 3)

cv2.imshow("detected circles", img)
cv2.waitKey(0)
