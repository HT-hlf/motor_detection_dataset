# coding:utf-8
# @Author     : HT
# @Time       : 2022/8/5 16:56
# @File       : augmention_dark.py
# @Software   : PyCharm


from PIL import Image
from PIL import ImageEnhance
import os
import cv2
import numpy as np
import random


def creat_dir(out_dir):
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

def brightnessEnhancement(root_path,img_name):#亮度增强
    image = Image.open(os.path.join(root_path, img_name))
    enh_bri = ImageEnhance.Brightness(image)
    brightness = random.randint(3,8)/100
    # brightness = random.randint(9, 25) / 100
    image_brightened = enh_bri.enhance(brightness)
    # cv2.imshow('0',image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return image_brightened,brightness

def rename(depth_path,name,houzui=False):
    if houzui:
        old_filename = depth_path + '/' + name.rstrip('jpg') + 'txt'
        new_filename = depth_path + '/bright_' + name.rstrip('jpg')+'txt'
    else:
        old_filename = depth_path + '/' + name
        new_filename = depth_path + '/bright_' + name
    os.rename(old_filename, new_filename)

raw_root_path=r'F:\Motor_detection_dataset\dataset\motor_detection_dataset_v1_no_chinese_yolov5_brightness'

# imageDir = os.path.join(raw_root_path,'images/train2017')
imageDir =r'F:\Motor_detection_dataset\test_image_sum'
# print(imageDir)
# saveDir = os.path.join(raw_root_path,'images/train2017_brightness')
# creat_dir(saveDir)
# labelDir = os.path.join(raw_root_path,'labels/train2017')
image_list=os.listdir(imageDir)
print(image_list)

for element in image_list:
    # imageDir = os.path.join(imageDir, element)
    print(1)
    saveImage, brightness = brightnessEnhancement(imageDir, element)
    # element_jpg=element.rstrip('tif')+'jpg'
    # saveName = "bright_" + element_jpg  # 保存的文件名
    # saveImage.save(os.path.join(saveDir, saveName))
    #
    # rename(labelDir, element_jpg)
