# coding:utf-8
# @Author     : HT
# @Time       : 2022/8/5 11:42
# @File       : read_image_resize.py
# @Software   : PyCharm

import cv2

img=cv2.imread(r'F:\Motor_detection_dataset\test_image_sum\20220616122644190.tif')
img_h,img_w,_=img.shape
print('原始的图片尺寸:宽-{} 高-{}'.format(img_w,img_h))
img_resize=cv2.resize(img,(640,480))
cv2.imshow('0',img)
cv2.imshow('resize',img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()