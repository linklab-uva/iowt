import os
import random

images = []

# image directory path
directory = '../../darknet/data/images'

# train.txt directory path
trainfile = '../../darknet/data/train.txt'
# val.txt directory path
valfile = '../../darknet/data/val.txt'

f = open(trainfile, "w")
f_val = open(valfile, "w")

for filename in os.listdir(directory):
	images.append(filename)

# shuffle images, use first 80% for training
random.shuffle(images)
num_images = int(len(images) * .8)
num_test_images = len(images) - num_images

# write training images and testing images to train.txt and val.txt
for i in range(num_images):
	f.write('data/images/' + images[i] + '\n')

reversed(images)
for i in range(num_test_images):
	f_val.write('data/images/' + images[i] + '\n')
