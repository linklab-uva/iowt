'''
Prints TP, FP, FN, TN for all classes, and average IoU across all classes for all TP.

Uses images with ground truth and detected coordinates in data/val_labels for calculations.
'''

import json

## turns (center_x, center_y, width, height) coordinates into (x1, y1, x2, y2) where (x1, y1) is top left corner of BB and (x2, y2) is bottom right corner of BB
def adjust_coordinates(center_x, center_y, width, height):
	scale_width = width / 2
	scale_height = height / 2
	return [center_x - scale_width, center_y - scale_height, center_x + scale_width, center_y + scale_height]

## calculate iou for two boxes with (x1, y1, x2, y2) coordinates
def iou(box1, box2):
    (box1_x1, box1_y1, box1_x2, box1_y2) = box1
    (box2_x1, box2_y1, box2_x2, box2_y2) = box2
    
    # Calculate the (yi1, xi1, yi2, xi2) coordinates of the intersection of box1 and box2. Calculate its Area.
    xi1 = max(box1_x1, box2_x1)
    yi1 = max(box1_y1, box2_y1)
    xi2 = min(box1_x2, box2_x2)
    yi2 = min(box1_y2, box2_y2)
    inter_width = max(xi2 - xi1, 0)
    inter_height = max(yi2 - yi1, 0)
    inter_area = inter_width * inter_height

    # Calculate the Union area by using Formula: Union(A,B) = A + B - Inter(A,B)
    box1_area = (box1_y2 - box1_y1) * (box1_x2 - box1_x1)
    box2_area = (box2_y2 - box2_y1) * (box2_x2 - box2_x1)
    union_area = (box1_area + box2_area) - inter_area
    
    # compute the IoU
    iou = inter_area / union_area
    
    return iou

val = '../../data/val.txt'
val_file = open(val, 'r')

tp_cup = 0
fn_cup = 0
fp_cup = 0
tn_cup = 0

tp_bottle = 0
fn_bottle = 0
fp_bottle = 0
tn_bottle = 0

tp_paper = 0
fn_paper = 0
fp_paper = 0
tn_paper = 0

iou_sum = 0
iou_count = 0

val_images = val_file.readlines()

min_iou_cup = 1
min_iou_cup_image = ''
min_iou_bottle = 1
min_iou_bottle_image = ''
min_iou_paper = 1
min_iou_paper_image = ''

for image in val_images:
	image_name = image.split('/')[2].split('.')[0]
	json_file = open('../../data/val_labels/' + image_name + '_out.json', 'r')
	found_objects = json.loads(json_file.read())['objects']

	txt_file = open('../../data/val_labels/' + image_name + '.txt', 'r')
	original_parameters = txt_file.read().split()
	original_label = original_parameters[0]
	adjusted_coordinates = adjust_coordinates(float(original_parameters[1]), float(original_parameters[2]), float(original_parameters[3]), float(original_parameters[4]))

	cup_label = original_label == '0'
	bottle_label = original_label == '1'
	paper_label = original_label == '2'

	num_cup = 0
	cup_coords = []
	num_bottle = 0
	bottle_coords = []
	num_paper = 0
	paper_coords = []
	for obj in found_objects:
		if(obj['name'] == 'cup'):
			num_cup += 1
			coords = obj['relative_coordinates']
			cup_coords.append(adjust_coordinates(coords['center_x'], coords['center_y'], coords['width'], coords['height']))
		elif(obj['name'] == 'bottle'):
			num_bottle += 1
			coords = obj['relative_coordinates']
			bottle_coords.append(adjust_coordinates(coords['center_x'], coords['center_y'], coords['width'], coords['height']))
		elif(obj['name'] == 'paper'):
			num_paper += 1
			coords = obj['relative_coordinates']
			bottle_coords.append(adjust_coordinates(coords['center_x'], coords['center_y'], coords['width'], coords['height']))
	
	# cup
	if(cup_label and num_cup >= 1):
		tp_cup += 1
		for coord in cup_coords:
			iou_val = iou(adjusted_coordinates, coord)
			if iou_val < min_iou_cup:
				min_iou_cup = iou_val
				min_iou_cup_image = image
			iou_sum += iou_val
			iou_count += 1
	elif(cup_label and num_cup == 0):
		fn_cup += 1
	elif((not cup_label) and num_cup >= 1):
		fp_cup += 1
	elif((not cup_label) and num_cup == 0):
		tn_cup += 1

	# bottle
	if(bottle_label and num_bottle >= 1):
		tp_bottle += 1
		for coord in bottle_coords:
			iou_val = iou(adjusted_coordinates, coord)
			if iou_val < min_iou_bottle:
				min_iou_bottle = iou_val
				min_iou_bottle_image = image
			iou_sum += iou_val
			iou_count += 1
	elif(bottle_label and num_bottle == 0):
		fn_bottle += 1
	elif((not bottle_label) and num_bottle >= 1):
		fp_bottle += 1
	elif((not bottle_label) and num_bottle == 0):
		tn_bottle += 1

	# paper
	if(paper_label and num_paper >= 1):
		tp_paper += 1
		print(paper_coords)
		for coord in paper_coords:
			iou_val = iou(adjusted_coordinates, coord)
			print(iou_val)
			if iou_val < min_iou_paper:
				min_iou_paper = iou_val
				min_iou_paper_image = image
			iou_sum += iou_val
			iou_count += 1
	elif(paper_label and num_paper == 0):
		fn_paper += 1
	elif((not paper_label) and num_paper >= 1):
		fp_paper += 1
	elif((not paper_label) and num_paper == 0):
		tn_paper += 1

	json_file.close()
	txt_file.close()

print('Total number of validation images:', len(val_images))
print('Cup data: true positive:', tp_cup, 'false negative:', fn_cup, 'false positive:', fp_cup, 'true negative:', tn_cup)
print('Bottle data: true positive:', tp_bottle, 'false negative:', fn_bottle, 'false positive:', fp_bottle, 'true negative:', tn_bottle)
print('Paper data: true positive:', tp_paper, 'false negative:', fn_paper, 'false positive:', fp_paper, 'true negative:', tn_paper)
print('Average IOU for all true positives:', iou_sum/iou_count)
print('cup:', min_iou_cup, min_iou_cup_image, '-- bottle:', min_iou_bottle, min_iou_bottle_image, '-- paper:', min_iou_paper, min_iou_paper_image)
val_file.close()
