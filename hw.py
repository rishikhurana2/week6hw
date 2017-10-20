import cv2
import numpy as np
import math

maxX = 0
maxY = 0
minX = 10000
minY = 10000

CFile = "rectangle-five-feet.jpg"
fileLocation = "rectangle-five-feet.jpg"
originalImage = cv2.imread(fileLocation)
Cimg = cv2.imread(CFile)

img_hsv = cv2.cvtColor(originalImage, cv2.COLOR_BGR2HSV)

cv2.imshow("Original Image", originalImage)
cv2.imshow("HSV Image", img_hsv)

THRESHOLD_MIN = np.array([0,125,0], np.uint8)
THRESHOLD_MAX = np.array([255,255,255], np.uint8)
frame_threshed = cv2.inRange(originalImage, THRESHOLD_MIN, THRESHOLD_MAX)
cv2.imshow("Treshed Image", frame_threshed)

frame_threshold = cv2.inRange(originalImage, THRESHOLD_MIN, THRESHOLD_MAX)
count = -1
image, contours, hierarchy = cv2.findContours(frame_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cont in contours:
	count = count + 1
	approx = cv2.approxPolyDP(cont, 0.1*cv2.arcLength(cont, True), True)
	if (cv2.contourArea(approx) > 3000):
		cv2.drawContours(Cimg, contours, count, (255,255,255), 5)
		for i in approx:
			if i[0][0] > maxX:
				maxX = i[0][0]
			if i[0][0] < minX:
				minX = i[0][0]
			if i[0][1] > maxY:
				maxY = i[0][1]
			if i[0][1] < minY:
				minY = i[0][1]

		width = maxX - minX
		height = maxY - minY
		focalLength = 480

		print (width)
		print (height)
		Distance = focalLength/width
		print (Distance)
cv2.imshow("Contour Image", Cimg)

cv2.waitKey(0)
