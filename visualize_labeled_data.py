# coding:utf-8
# @Author     : HT
# @Time       : 2022/8/4 16:31
# @File       : visualize_labeled_data.py
# @Software   : PyCharm


import cv2
import os


classes=['y0','y1','y2','y3','w0','w1','w2','w3','scratch','shed','bolt']
count_list  =[   0,0,0,0,0,0,0,0,0,0,0]
def draw_box_in_single_image(image_path, txt_path,jpg_path):
    # 读取图像
    image = cv2.imread(image_path)

    # 读取txt文件信息
    def read_list(txt_path):
        pos = []
        with open(txt_path, 'r') as file_to_read:
            while True:
                lines = file_to_read.readline()  # 整行读取数据
                if not lines:
                    break
                # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
                p_tmp = [float(i) for i in lines.split(' ')]
                pos.append(p_tmp)  # 添加新读取的数据
                # Efield.append(E_tmp)
                pass
        return pos


    # txt转换为box
    def convert(size, box):
        xmin = (box[1]-box[3]/2.)*size[1]
        xmax = (box[1]+box[3]/2.)*size[1]
        ymin = (box[2]-box[4]/2.)*size[0]
        ymax = (box[2]+box[4]/2.)*size[0]
        box = (int(xmin), int(ymin), int(xmax), int(ymax))
        return box

    pos = read_list(txt_path)
    print(pos)
    tl = int((image.shape[0]+image.shape[1])/2)
    lf = max(tl-1,1)
    for i in range(len(pos)):
        # label = str(int(pos[i][0]))
        label = int(pos[i][0])
        count_list[label]=count_list[label]+1
        print('------------count_list-------------')
        print(count_list)
        print('------------count_list-------------')
        # print('label is '+label)
        box = convert(image.shape, pos[i])
        image = cv2.rectangle(image,(box[0], box[1]),(box[2],box[3]),(0,255,0),2)
        cv2.putText(image,classes[label],(box[0],box[1]-2), 0, 2, [0,255,0], thickness=3, lineType=cv2.LINE_AA)
        pass
    # cv2.imshow('0', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    if pos:
        cv2.imwrite(jpg_path, image)
    else:
        print('None')


    print('./VOCData/see_images/{}.png'.format(image_path.split('\\')[-1][:-4]))
    # cv2.imshow("images", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

root_path=r"F:\Motor_detection_dataset\dataset\motor_detection_dataset_v1_no_chinese_VOCdevkit\VOC2007"
img_folder = os.path.join(root_path,'JPEGImages')
img_list = os.listdir(img_folder)
img_list.sort()

label_folder = os.path.join(root_path,'labels')
label_list = os.listdir(label_folder)
label_list.sort()

save_folder = os.path.join(root_path,'visual_labeled_data')
if not os.path.isdir(save_folder):
    os.makedirs(save_folder)
for element in img_list:
    image_path = img_folder + "\\" + element
    print(image_path)
    element_txt = element.rstrip('tif') + 'txt'
    element_jpg = element.rstrip('tif') + 'jpg'
    jpg_path = save_folder + "\\" + element_jpg
    txt_path = label_folder + "\\" + element_txt
    draw_box_in_single_image(image_path, txt_path,jpg_path)
print('------------last count_list-------------')
print(count_list)
print('------------last count_list-------------')
