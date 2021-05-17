import shutil
import os
import sys
import re

""" 
Rename YOLO annotation txt files to match images names and offset count by 1
""" 

# directory with text files
video = 'Overhead-Paper'
directory = '../../final_annotations/' + video + '/10_' + video
prefix = 'g_'

for filename in os.listdir(directory):
	new_name = re.sub('frame_0{2,3}', '', filename)
	new_name = re.sub('.txt', '', new_name)

	# ignore object names file
	if(filename != 'obj.names'):
		new_name = int(new_name)
		new_name += 1
		new_name = prefix + str(new_name) + '.txt'
	os.rename(directory+'/'+filename, directory+'/'+new_name)


