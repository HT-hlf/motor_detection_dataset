# coding:utf-8
# @Author     : HT
# @Time       : 2022/8/4 16:48
# @File       : visualize_labeled_data1.py
# @Software   : PyCharm

import xml.etree.ElementTree as ET
import os, cv2

xml_file = r'F:\电机检测项目\dataset\motor_detection_dataset_v1\annotation/20220719095627881.xml'
# tree = ET.parse(xml_file)
# root = tree.getroot()

f = open(xml_file)
xml_text = f.read()
root = ET.fromstring(xml_text)

imgfile = r'F:\电机检测项目\dataset\motor_detection_dataset_v1\image/20220719095627881.tif'
im = cv2.imread(imgfile)
for object in root.findall('object'):
    object_name = object.find('name').text
    Xmin = int(object.find('bndbox').find('xmin').text)
    Ymin = int(object.find('bndbox').find('ymin').text)
    Xmax = int(object.find('bndbox').find('xmax').text)
    Ymax = int(object.find('bndbox').find('ymax').text)
    print(object)
    color = (0, 0, 255)
    cv2.rectangle(im, (Xmin, Ymin), (Xmax, Ymax), color, 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(im, object_name, (Xmin, Ymin - 7), font, 0.5, (6, 230, 230), 2)
    print(im.shape)
    im_height,im_width,_=im.shape
    im_resize=cv2.resize(im,(im_width//10,im_height//10))
    cv2.imshow('img', im_resize)
    cv2.imwrite(r'F:\test/labeled.jpg', im)
    cv2.waitKey(0)
f.close()