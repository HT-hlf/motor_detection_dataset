# coding:utf-8
# @Author     : HT
# @Time       : 2022/7/27 22:00
# @File       : copy_labled_data.py
# @Software   : PyCharm


import os
import cv2
import numpy as np
import shutil
import random


image_path_list=['F:\doing\Motor_detection_dataset\电机外观图片拍图',]
dist_root_path='F:\doing\Motor_detection_dataset\dataset\motor_detection_dataset_all_v1'

def creat_dir(out_dir):
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

def copy_dataset(raw_root_path_element,dist_root_path,image_list):
    for element in image_list:

        element_path = os.path.join(raw_root_path_element, element)

        # print(element.split('.')[-1])
        if element.split('.')[-1] == 'tif':

            dist_element_image_path = os.path.join(dist_root_path, 'image',element)
            element_xml=element.rstrip('tif') + 'xml'
            dist_element_annotation_path = os.path.join(dist_root_path, 'annotation', element_xml)
            print(element_path)
            shutil.copy(element_path, dist_element_image_path)
        else:
            image_list1 = os.listdir(element_path)
            copy_dataset(element_path, dist_root_path, image_list1)

dist_image_path = os.path.join(dist_root_path, 'image')
creat_dir(dist_image_path)
for path in image_path_list:
    raw_root_path = path

    raw_root_list=os.listdir(raw_root_path)


    for raw_root_element in raw_root_list:
        raw_root_path_element=os.path.join(raw_root_path, raw_root_element)
        print(raw_root_path_element)
        image_list = os.listdir(raw_root_path_element)

        copy_dataset(raw_root_path_element, dist_root_path, image_list)
        # for element in image_list:
        #
        #     element_path=os.path.join(raw_root_path_element, element)
        #
        #     # print(element.split('.')[-1])
        #     if element.split('.')[-1]=='tif':
        #
        #         dist_element_path=os.path.join(dist_root_path, element)
        #         print(element_path)
        #
        #         shutil.copy(element_path, dist_element_path)
        #     else:
        #         image_list1 = os.listdir(element_path)
        #         for element1 in image_list1:
        #             element_path1 = os.path.join(element_path, element1)
        #             dist_element_path = os.path.join(dist_root_path, element)
        #             print(element_path)
        #
        #             shutil.copy(element_path1, dist_element_path)



