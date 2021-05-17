'''
Copy all txt files from corresponding images in val.txt to folder data/val_labels.
Used to compare ground truth coordinates with detected coordinates (detected coordinated are parsed and placed into data/val_labels with parse_results_json.py.
'''

from shutil import copyfile
import os

val = '../../data/val.txt'

val_file = open(val, 'r')
images = val_file.readlines()
val_file.close()

os.system('mkdir ../../data/val_labels')

for image in images:
	txt_name = image_name = image.split('/')[2].split('.')[0] + '.txt'
	copyfile('../../data/images/' + txt_name, '../../data/val_labels/' + txt_name)
