# coding:utf-8
# @Author     : HT
# @Time       : 2022/7/28 21:19
# @File       : rename_dataset.py
# @Software   : PyCharm

import os
import cv2
import numpy as np
import shutil
import random


image_path=r'F:\电机检测项目\dataset\motor_detection_dataset_v1_no_chinese\image'
annotation_path=r'F:\电机检测项目\dataset\motor_detection_dataset_v1_no_chinese\annotation'

image_path_list = os.listdir(image_path)

for element in image_path_list:
    element_path = os.path.join(image_path, element)
    print(element_path)
    image_list = os.listdir(raw_root_path_element)

###代码没写完，不可用