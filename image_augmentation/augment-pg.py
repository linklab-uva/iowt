import os, re
import numpy as np
import imageio
import imgaug as ia
from imgaug import augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
from convert_YOLOtoimgaug import convertYolov3BBToImgaugBB, convertImgaugBBToYolov3BB

augments = {
	# 'brightness': iaa.MultiplyBrightness((0.5, 1.5)),
	# 'blur': iaa.GaussianBlur(sigma=(0.0, 2.5)),
	'fliplr': iaa.Fliplr(1),
	# 'flipud': iaa.Flipud(1),
	# 'scale': iaa.Affine(scale=(0.75, 1.25)),
	# 'rotate': iaa.Affine(rotate=(-45, 45)),
	# 'translate': iaa.Affine(translate_px={"x": (-20, 20), "y": (-20, 20)}),
}

dataspace = '../pg-iowt/darknet/data/aug_dataset/'

def augment_images(image_path):
	counter = 0
	for img in os.listdir(image_path):
		if img.endswith('JPG'):	
			augment_image(image_path, img, counter)

		counter += 1

def augment_image(image_path, img, counter):
	image = imageio.imread(image_path + '/' + img) # read image
	height, width, depth = image.shape

	# open corresponding txt file
	image_name = img.split('.')[0]
	txt_file = open(image_path + '/' + image_name + '.txt', 'r')

	# create array for all bounding boxes
	bb_array = []
	for line in txt_file:
		vals = re.split('\s+', line.rstrip())

		# get imgaug coords
		imgaug_vals = convertYolov3BBToImgaugBB(vals, height, width)

		bb_array.append(ia.BoundingBox(x1 = imgaug_vals[1],
						y1 = imgaug_vals[2],
						x2 = imgaug_vals[3],
						y2 = imgaug_vals[4],
						label = imgaug_vals[0]))

	bbs = BoundingBoxesOnImage(bb_array, shape=image.shape)

	for aug_type in augments:
		print(img, aug_type, counter)
		seq = iaa.Sequential([ augments[aug_type]])

		image_aug, bbs_aug = seq(image=image, bounding_boxes=bbs)

		imageio.imwrite(image_path + '/' + image_name + '_' + aug_type + '.jpg', image_aug)

		aug_label = open(image_path + '/' + image_name + '_' + aug_type + '.txt', 'w')
		for i in range(len(bbs_aug.bounding_boxes)):
			aug_bb = bbs_aug.bounding_boxes[i]
			yolo_aug_bb = convertImgaugBBToYolov3BB([aug_bb.label, aug_bb.x1, aug_bb.y1, aug_bb.x2, aug_bb.y2], height, width)
			# print before and after augmentation bounding boxes
			image_before = bbs.draw_on_image(image, thickness=2)
			image_after = bbs_aug.draw_on_image(image_aug, thickness=2, color=[0, 0, 255])

			imageio.imwrite(image_name + '-before.jpg', image_before)  #write all changed images
			imageio.imwrite(image_name + '-after.jpg', image_after)  #write all changed images

			# print(aug_bb)
			
			# print(yolo_aug_bb)
			aug_label.write(str(yolo_aug_bb[0]) + ' ' + str(yolo_aug_bb[1]) + ' ' + str(yolo_aug_bb[2]) + ' ' + str(yolo_aug_bb[3]) + ' ' + str(yolo_aug_bb[4]) + '\n')

# for root, dirs, files in os.walk(dataspace):
# 	if not root.endswith('json_annotations') or not root.endswith('movies'):
# 		if len(files) > 0:
# 			augment_images(root)

augment_image('.', 'IMG_5672.JPG', 0)