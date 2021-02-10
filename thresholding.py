import cv2 as cv
import numpy as np 

img = cv.imread("test_images/boston.png")
cv.imshow("Original", img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# Simple thresholding 
# What it does is that all the pixel values which are less than 150 (threshold value) is set to 0 which is black where as all the pixel values greater than 150(threshold value) is set to 255 white.
threshold, thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)  
cv.imshow("Simple Thresh",thresh)
# Creating an inverse thresholded image 
# All the pixel values which are less than 150 (threshold value) is set to 255 which is white where as all the pixel values greater than 150(threshold value) is set to 0 black.
threshold, thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow("Inverse Thresholded",thresh_inv) 

cv.waitKey(0)