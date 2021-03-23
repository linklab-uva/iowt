import numpy as np
import imageio
import imgaug as ia
from imgaug import augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
import os

def do_aug(aug_type, image_path, label_path, aug_image_path, aug_label_path):

	aug = None
	if aug_type == 'scale':
		aug = iaa.Affine(scale=(0.5, 1.5))
	elif aug_type == 'brightness':
		aug = iaa.WithBrightnessChannels(iaa.Add((-50, 50)))
	elif aug_type =='blur':
		aug = iaa.GaussianBlur(sigma=(0.0, 2.5))
	elif aug_type =='huesat':
		aug = iaa.WithHueAndSaturation(iaa.WithChannels(0, iaa.Add((0, 50))))
	elif aug_type =='temp':
		aug = iaa.ChangeColorTemperature((1100, 10000))
	elif aug_type =='flip':
		aug =  iaa.Fliplr(1)

	counter = 0
	for img in os.listdir(image_path):
		print(aug_type, counter)
		image = imageio.imread(image_path + '/' + img) #read you image
		image_name = img.split('.')[0]

		box = open(label_path + '/' + image_name + '.txt', 'r').read()
		values = box.split()
		bb = BoundingBox(x1=float(values[0]), y1=float(values[1]), x2=float(values[2]), y2=float(values[3]), label=values[4])

		bbs = BoundingBoxesOnImage([ bb ], shape=image.shape)

		seq = iaa.Sequential([ aug ])

		images_aug, bbs_aug = seq(image=image, bounding_boxes=bbs)

		imageio.imwrite(aug_image_path + '/' + image_name + '_' + aug_type + '.jpg', images_aug)

		aug_label = open(aug_label_path + '/' + image_name + '_' + aug_type + '.txt', 'w')

		# copying original bounding box, not using any augmentation that would change box		
		# aug_label.write(box)

		# Bounding boxes come out correct but in the wrong order, not consistent
		aug_label.write(str(bbs_aug[0].x1) + ' ' + str(bbs_aug[0].y1) + ' ' + str(bbs_aug[0].x2) + ' ' + str(bbs_aug[0].y2) + ' ' + str(bbs_aug[0].label)) 

		counter += 1

def do_all_aug(image_path, label_path, aug_image_path, aug_label_path):
	do_aug('scale', image_path, label_path, aug_image_path, aug_label_path)
	do_aug('brightness', image_path, label_path, aug_image_path, aug_label_path)
	# do_aug('blur', image_path, label_path, aug_image_path, aug_label_path)
	# do_aug('huesat', image_path, label_path, aug_image_path, aug_label_path)
	# do_aug('temp', image_path, label_path, aug_image_path, aug_label_path)
	do_aug('flip', image_path, label_path, aug_image_path, aug_label_path)

do_all_aug('images_copy', 'labels_copy', 'aug_images', 'aug_labels')

