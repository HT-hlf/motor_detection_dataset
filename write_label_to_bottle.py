import os

def creat_dir(out_dir):
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

filepath=r'F:\doing\Motor_detection\datasets_second_remove_noise_add_third_check_add_aug\motor_detection_dataset_v2\labels\train2017'
filepath_bottle=filepath+'_bottle'
creat_dir(filepath_bottle)
class_name = ['y0','y1','y2','y3','w0','w1','w2','w3','scratch','shed','bolt']
class_idx= [0,1,2,3,4,5,6,7]
pathDir = os.listdir(filepath)
for s in pathDir:
	if s== 'classes.txt':
		continue
	# s='3633_36.txt'
	print(s)
	newDir = os.path.join(filepath, s)
	out_file = open(os.path.join(filepath_bottle, s), 'w')
	if os.path.isfile(newDir):
		if os.path.splitext(newDir)[1] == ".txt":
			with open(newDir, "r") as f:
				data = f.readlines()
				# print(data)
				# print(int(data[0][0]))
				for i in range(len(data)):
					data_i=data[i]
					print(data_i)
					out_file.write(data_i)
					data_i_split=data_i.split()
					x=int(data_i_split[0])
					if x in class_idx:
						data_i_split[0]='10'
						data_i_split_str=' '.join(data_i_split)
						print(data_i_split_str)
						out_file.write(data_i_split_str+'\n')
					# print(x)
	out_file.close()


				# print(data)

print(class_name)








