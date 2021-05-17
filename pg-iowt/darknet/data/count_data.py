import os
dataspace = 'dataset'

datatypes_count = {
	'gloves': {'images': 0, 'videos': 0, 'total': 0, 'percent_vid': 0, 'percent_image': 0},
	'suction': {'images': 0, 'videos': 0, 'total': 0, 'percent_vid': 0, 'percent_image': 0},
	'holster': {'images': 0, 'videos': 0, 'total': 0, 'percent_vid': 0, 'percent_image': 0},
	'knife': {'images': 0, 'videos': 0, 'total': 0, 'percent_vid': 0, 'percent_image': 0},
	'ligasure': {'images': 0, 'videos': 0, 'total': 0, 'percent_vid': 0, 'percent_image': 0},
	'stapler': {'images': 0, 'videos': 0, 'total': 0, 'percent_vid': 0, 'percent_image': 0},
}

num_images = {
	'images': 0,
	'videos': 0,
}

num_videos = 0

datatypes_id = {
	'0': 'gloves',
	'1': 'holster',
	'2': 'knife',
	'3': 'ligasure',
	'4': 'stapler',
	'5': 'suction',
}

for root, dirs, files in os.walk(dataspace):
	if root.endswith('json_annotations') or root.endswith('movies'):
		continue
		
	if root.endswith('images'):
		image = True
	else:
		image = False
		if root[-1].isnumeric(): num_videos += 1
	
	for text in files:
		text_path = root + '/' + text
		if text.endswith('txt'):
			if image: num_images['images'] += 1
			else: num_images['videos'] += 1
			
			text_file = open(text_path, 'r')
			annotations = text_file.readlines()
			text_file.close()
			for ann in annotations:
				vals = ann.split()
				type_id = vals[0]
				datatype = datatypes_id[type_id]
				
				if image:
					datatypes_count[datatype]['images'] += 1
				else:
					datatypes_count[datatype]['videos'] += 1


for datatype in datatypes_count.keys():
	datatypes_count[datatype]['total'] = datatypes_count[datatype]['images'] + datatypes_count[datatype]['videos']
	datatypes_count[datatype]['percent_vid'] = datatypes_count[datatype]['videos'] / datatypes_count[datatype]['total']
	datatypes_count[datatype]['percent_image'] = datatypes_count[datatype]['images'] / datatypes_count[datatype]['total']
					
print(datatypes_count)
print(num_images)
print('num_videos: ' + str(num_videos))
				
