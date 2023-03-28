#Đầu vào đưa vào 2 ảnh, đầu ra là sự khác biệt của 2 bức ảnh

import cv2
import imutils 
import numpy as np

#Load the image
img1 = cv2.imread(r'image\img_data_3.png')
img1 = cv2.resize(img1, (600, 600))
img2 = cv2.imread(r'image\img_data_3_lv3out.png')
img2 = cv2.resize(img2, (600, 600))

#Grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#find the difference
diff = cv2.absdiff(gray1, gray2)
# cv2.imshow('diff(img1, img2)', diff)

#Apply threshold
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# cv2.imshow('Threshold', thresh)

#Dilation
kernel = np.ones((5,5), np.uint8)
dilate = np.ones(thresh, kernel, iterations=2)
# cv2.imshow('Dilation', dilate)

#Find contours
contours = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

#Loop over each contour
for contour in contours:
    if cv2.contourArea(contour) > 100:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img1, (x, y), (x+w, y+h), (0,0,255), 2)
        cv2.rectangle(img2, (x, y), (x+w, y+h), (0,0,255), 2)
        
#show final images
x = np.zeros((600, 10, 3), np.uint8)
result = np.hstack((img1, img2))
cv2.imshow("diffences", kernel)

# cv2.imshow('Original Img', img1)
# cv2.imshow('Edited Img', img2)

cv2.waitKey(0)
cv2.destroyAllWindows

