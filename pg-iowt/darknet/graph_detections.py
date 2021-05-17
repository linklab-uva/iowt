from matplotlib import pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
from collections import Counter
import numpy as np
import os
import json

dataspace = 'data/mock_or/results/'
graph_folder = 'data/mock_or/graphs/'

for json_file in os.listdir(dataspace):

	# get mock_orx from mock_orx_result.json
	vid_name = json_file.split('.')[0][0:8]
		
	x_axis = np.array([])
	
	object_types = {
		0: {'name':'gloves', 'y': np.array([])},
		1: {'name':'holster', 'y': np.array([])},
		2: {'name':'knife', 'y': np.array([])},
		3: {'name':'ligasure', 'y': np.array([])},
		4: {'name':'stapler', 'y': np.array([])},
		5: {'name':'suction', 'y': np.array([])},
	}
	
	read_results = open(dataspace+json_file, 'r')
	frames = json.loads(read_results.read())
	read_results.close()
	
	for frame in frames:
		frame_num = frame['frame_id']
		
		
		object_counts = {
			0: 0,
			1: 0,
			2: 0,
			3: 0,
			4: 0,
			5: 0
		}

		
		for detected_objects in frame['objects']:
			single_found_object = detected_objects['class_id']
			object_counts[single_found_object] += 1
#			single_found_object = detected_objects['class_id']
#			if frames.index(frame) > 50:
#				fifty_frames_prev_index = frames.index(frame) - 50
#				frame_fifty_prev = frames[fifty_frames_prev_index]
#				number_detected_object_type = 
#				for prev_detected_objects in frame_fifty_prev['objects']:
#					prev_found_object = prev_detected_objects['class_id']
#					
#					if single_found_object == prev_found_object:
#						object_counts[single_found_object] += 1
#			else:
#				object_counts[single_found_object] += 1

		x_axis = np.append(x_axis, frame_num)
		
		# append object count to each y array in object_types
		for object_num in object_counts.keys():
			object_types[object_num]['y'] = np.append(object_types[object_num]['y'], object_counts.get(object_num))

	for object_num in object_types:
		name = object_types[object_num]['name']
		plt.plot(x_axis, object_types[object_num]['y'])
		# x_y_spline = make_interp_spline(x_axis, object_types[object_num]['y'], k=6)
		# x_ = np.linspace(x_axis.min(), x_axis.max(), 500) # may need to alter if changing frame counts
		# y_ = x_y_spline(x_)
		# plt.plot(x_, y_)
		
		plt.xlabel('Frame Number')
		plt.ylabel('Instance Count')
		plt.title(name)
		fig = plt.gcf()
		fig.set_size_inches(24, 6)
		plt.yticks(np.arange(0, object_types[object_num]['y'].max() + 1, step=1))
		file_name = json_file.split('.')[0]
		plt.savefig(graph_folder + vid_name + '_' + name + '.png', bbox_inches='tight')
		
		plt.clf()

