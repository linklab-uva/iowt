aug_types = ['brightness', 'blur', 'huesat', 'temp']

trainfile = open('train.txt', 'r')
training_images = trainfile.readlines()
trainfile.close()

new_trainfile = open('aug_train.txt', 'w')

for imgpath in training_images:
	imgfile = imgpath.split('/')[2]
	imgname = imgfile.split('.')[0]
	new_trainfile.write('data/aug_images/' + imgname + '.jpg\n')
	for aug_type in aug_types:
		new_imgpath = 'data/aug_images/' + imgname + '_' + aug_type + '.jpg\n'
		new_trainfile.write(new_imgpath)

new_trainfile.close()

