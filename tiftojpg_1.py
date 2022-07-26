# coding:utf-8
# @Author     : HT
# @Time       : 2022/8/5 17:29
# @File       : tiftojpg.py
# @Software   : PyCharm

import cv2
import os



root_path=r"F:\doing\Motor_detection_dataset\third_dataset\receive\10.10D\10.10D"
save_path=root_path+"jpg"
img_list = os.listdir(root_path)
img_list.sort()


if not os.path.isdir(save_path):
    os.makedirs(save_path)
count=1
for element in img_list:
    image_path = root_path + "\\" + element
    # print(image_path)

    # element_jpg = element.rstrip('tif') + 'jpg'
    # jpg_path = save_path + "\\first_collect_" + str(count)+'.jpg'
    jpg_path = save_path + "\\" + element.rstrip('.tif') + '.jpg'
    # print(jpg_path)  
    image = cv2.imread(image_path)

    # cv2.imshow('0', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.imwrite(jpg_path, image)
    count+=1

