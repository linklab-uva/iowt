import os
from shutil import copyfile

image_dir = 'data/images'
model = 'model-test'

for filename in os.listdir(image_dir):
	if filename.endswith('txt'): continue
	if model == 'baseline':
		os.system('./darknet detector test coco-adj.data cfg/yolov3.cfg yolov3.weights data/only_images/' + filename + ' -dont_show')
		name = filename.split('.')[0]
		copyfile('predictions.jpg', 'models/' + model + '/out_images/' + name + '_out.jpg')

	else:
		os.system('./darknet detector test models/' + model + '/obj.data models/' + model + '/obj.cfg models/' + model + '/obj_best.weights data/only_images/' + filename + ' -dont_show')
		name = filename.split('.')[0]
		copyfile('predictions.jpg', 'models/' + model + '/out_images/' + name + '_out.jpg')
