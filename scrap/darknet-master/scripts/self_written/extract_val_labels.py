from shutil import copyfile

val = '../../data/val.txt'

val_file = open(val, 'r')
images = val_file.readlines()

for image in images:
	txt_name = image_name = image.split('/')[2].split('.')[0] + '.txt'
	copyfile('../../data/labels/' + txt_name, '../../data/val_labels/' + txt_name)
