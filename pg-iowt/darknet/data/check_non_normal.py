
import os
dataspace = 'dataset/table/table0'

def check_non_normal():
	count = 0
	for root, dirs, files in os.walk(dataspace):

		if root.startswith(dataspace):
			if not root.endswith('json_annotations') or not root.endswith('movies'):
				for text in files:
					text_path = root + '/' + text
					if text.endswith('txt'):
						text_file = open(text_path, 'r')
						annotations = text_file.readlines()
						text_file.close()
						for ann in annotations:
							vals = ann.split()
							for i in range(1, len(vals)):
								if float(vals[i]) > 1 or float(vals[i]) < 0:
									count += 1
									print('txt file path:', text_path)
									print('off value:', vals[i])
									
	print('total wrong values:', count)

check_non_normal()
