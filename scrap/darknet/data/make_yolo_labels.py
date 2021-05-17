import os

labels_dir = 'labels/'
output_label = 'yolo-images/'

for label in os.listdir(labels_dir):
	if label.split('.')[1] == 'txt':
		old_label = open(labels_dir + label, 'r')
		label_vals = old_label.read().split()
		old_label.close()
		
		new_label_val = '0'
		if(label_vals[0] == '0'):	
			new_label_val = '41'

		elif(label_vals[0] == '1'):	
			new_label_val = '39'

		new_txtfile = open(output_label + label, 'w')
		new_txtfile.write(new_label_val + ' ' + label_vals[1] + ' ' + label_vals[2] + ' ' + label_vals[3] + ' ' + label_vals[4])
		new_txtfile.close()
