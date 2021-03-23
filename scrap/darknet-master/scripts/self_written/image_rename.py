import os

#directory with images
video = 'Overhead-Paper'
directory = '../../final_annotations/' + video + '/extracted_images_' + video
prefix = 'g_'

for filename in os.listdir(directory):
	new_name = prefix + filename
	os.rename(directory+'/'+filename, directory+'/'+new_name)
