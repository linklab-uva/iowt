import sys
import os

"""
Re-define index for label in Overhead-Paper txt files -> change 0 (for paper) to 2 (for paper)
"""

# directory with txt files
video = sys.argv[1]
number = sys.argv[2]
directory = '../../final_annotations/' + video + '/' + number + '_' + video + '_real'

for filename in os.listdir(directory):
	if filename == 'obj.names':
		continue

	txt_file = open(directory + '/' + filename, 'r')
	box = txt_file.read()
	box = box.split(' ', 1)[1]
	txt_file.close()

	txt_file = open(directory + '/' + filename, 'w')
	txt_file.seek(0)
	txt_file.write('2 ' + box)
	txt_file.close()
