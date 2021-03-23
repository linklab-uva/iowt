
from pathlib import Path
import json
import os
dataspace = 'models/model5'

count = 0
result_path = './result.json'
read_results = open(result_path, 'r')
results_list = json.loads(read_results.read())
read_results.close()

model = 'model5'
save_path = 'models/' + model + '/out_images/class_detections/'

class_detections = {
	0: {
		'tp': [0, []],
		'fp': [0, []],
		'fn': [0, []],
		'label': 'gloves',
	}, 
	1: {
		'tp': [0, []],
		'fp': [0, []],
		'fn': [0, []],
		'label': 'holster',
	}, 
	2: {
		'tp': [0, []],
		'fp': [0, []],
		'fn': [0, []],
		'label': 'knife',
	}, 
	3: {
		'tp': [0, []],
		'fp': [0, []],
		'fn': [0, []],
		'label': 'ligasure',
	}, 
	4: {
		'tp': [0, []],
		'fp': [0, []],
		'fn': [0, []],
		'label': 'stapler',
	}, 
	5: {
		'tp': [0, []],
		'fp': [0, []],
		'fn': [0, []],
		'label': 'suction',
	},  
}


for img_ann in results_list:
	image_path = img_ann['filename']
	true_labels = []

	# get ground truth label file
	txt_file_path = image_path.split('.')[0] + '.txt'
	try: txt_file = open(txt_file_path, 'r')
	except FileNotFoundError: continue

	# save ground truth detections to list
	for line in txt_file.readlines():
		label = line.split()
		true_labels.append(int(label[0]))

	txt_file.close()

	# for each annotation in detections
	for ann in img_ann['objects']:
		detected_label = ann['class_id']
		# if detected class is present in ground truth list -> increment TP
		if detected_label in true_labels:
			class_detections[detected_label]['tp'][0] += 1
			class_detections[detected_label]['tp'][1].append(image_path)
			true_labels.remove(detected_label)
		# else -> increment FP
		else:
			class_detections[detected_label]['fp'][0] += 1
			class_detections[detected_label]['fp'][1].append(image_path)

	# for all remaining values in ground truth list -> increment FN
	for label in true_labels:
		class_detections[label]['fn'][0] += 1
		class_detections[label]['fn'][1].append(image_path)

# print all data to txt files
total_counts = open(save_path + 'total_counts.txt', 'w')

for class_num in class_detections.keys():
	class_type = class_detections[class_num]

	with open(save_path + class_type['label'] + '_tp.txt', 'w') as f:
    		for img in class_type['tp'][1]:
        		f.write("%s\n" % img)

	with open(save_path + class_type['label'] + '_fp.txt', 'w') as f:
    		for img in class_type['fp'][1]:
        		f.write("%s\n" % img)

	with open(save_path + class_type['label'] + '_fn.txt', 'w') as f:
    		for img in class_type['fn'][1]:
        		f.write("%s\n" % img)

	total_counts.write(str(class_type['label']) + ' TP total:' + str(class_type['tp'][0]) + '\n')
	total_counts.write(str(class_type['label']) + ' FP total:' + str(class_type['fp'][0]) + '\n')
	total_counts.write(str(class_type['label']) + ' FN total:' + str(class_type['fn'][0]) + '\n')

total_counts.close()
		



