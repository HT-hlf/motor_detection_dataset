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


image_path_list=['F:\电机检测项目\电机外观图片拍图',]
annotation_path=r'F:\电机检测项目\annotation'
dist_root_path='F:\电机检测项目\dataset\motor_detection_dataset_v1'

data_num=0

def creat_dir(out_dir):
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

def copy_dataset(raw_root_path_element,dist_root_path,image_list):
    global data_num
    for element in image_list:

        element_path = os.path.join(raw_root_path_element, element)

        # print(element.split('.')[-1])
        if element.split('.')[-1] == 'tif':

            dist_element_image_path = os.path.join(dist_root_path, 'image',element)
            annotation_path_list = os.listdir(annotation_path)
            element_xml=element.rstrip('tif') + 'xml'
            element_annotation_path = os.path.join(annotation_path,element_xml)
            dist_element_annotation_path = os.path.join(dist_root_path, 'annotation', element_xml)
            print(element_annotation_path)
            print(element_path)
            data_num = data_num + 1
            # if element_xml in annotation_path_list:
            #     data_num=data_num+1
                # shutil.copy(element_path, dist_element_image_path)
                # shutil.copy(element_annotation_path, dist_element_annotation_path)
        else:
            image_list1 = os.listdir(element_path)
            copy_dataset(element_path, dist_root_path, image_list1)

# dist_image_path = os.path.join(dist_root_path, 'image')
# dist_annotation_path = os.path.join(dist_root_path, 'annotation')
# creat_dir(dist_image_path)
# creat_dir(dist_annotation_path)
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

print('样本数量：{}'.format(data_num))



