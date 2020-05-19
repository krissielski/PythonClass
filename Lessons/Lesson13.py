#Lesson13 - pip and OpenCV

#pip    - pythons package-management system
#OpenCv - Image Processing / Computer Vision / Graphics
#numPy  - math package - Arrays/Matricies

#python --version
#python -m pip install opencv-python
#python -m pip install --user numpy

import cv2
import numpy as np

#   (0,0)-----> (+X,0)
#     |
#     |
#     |
#   (0,+Y)

#Create Image Space
img_length = 400
img_width  = 300
img_dim    = 3
#                |------  touple -------------|
img = np.zeros(  (img_length,img_width,img_dim), np.uint8)


#          img  ( center)  r   (   color   )  Thickness
cv2.circle(img, (  0,  0), 10, (255,255,255), -1 )
cv2.circle(img, ( 50, 50), 10, (255,  0,  0),  -1 )
cv2.circle(img, (150,400), 10, (  0,255,  0), -1 )
cv2.circle(img, (299,399), 10, (  0,  0,255), -1 )


cv2.rectangle(img,  (140,190), (160,210) , (150,150,150), 2 )

print(img[0][0][1] )


cv2.imshow('image', img)
