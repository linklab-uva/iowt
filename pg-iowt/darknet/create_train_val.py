import random
import os

dataspace = 'data/dataset'

# split dataset into train-val with mixed and table folders making up the val.txt and all other folders included in train.txt
def trainval1():
    val_file = open('data/val.txt', 'a')
    train_file = open('data/train.txt', 'a')

    for root, dirs, files in os.walk(dataspace):

        if root.startswith(dataspace + '/mixed') or root.startswith(dataspace + '/table'):
            if not root.endswith('json_annotations') or not root.endswith('movies'):
                for img in files:
                    if img.endswith('JPG'):
                        name = img.split('.')[0]
                        if os.path.exists(root + '/' + name + '.txt'):
                            img_path = root + '/' + img
                            val_file.write(img_path + '\n')

        else:
            if not root.endswith('json_annotations') or not root.endswith('movies'):
                for img in files:
                    if img.endswith('JPG'):
                        name = img.split('.')[0]
                        if os.path.exists(root + '/' + name + '.txt'):
                            img_path = root + '/' + img
                            train_file.write(img_path + '\n')

    val_file.close()
    train_file.close()


# split all folders in dataset for 80-20 train-val set
def trainval2():
	val_file = open('data/val.txt', 'w')
	train_file = open('data/train.txt', 'w')

	val_file.close()
	train_file.close()

	val_file = open('data/val.txt', 'a')
	train_file = open('data/train.txt', 'a')

	for root, dirs, files in os.walk(dataspace):
		img_list = []
		img_path = ''

		if root.startswith(dataspace):
			if not root.endswith('json_annotations') or not root.endswith('movies'):
				for img in files:
					if img.endswith('JPG'):
						img_list.append(img)

		list_size = len(img_list)
		random.shuffle(img_list)
		stop_number = int(0.8*list_size)

		for i in range(stop_number):
			img_path = root + '/' + img_list[i]
			train_file.write(img_path + '\n')
		for i in range(stop_number, list_size):
			img_path = root + '/' + img_list[i]
			val_file.write(img_path + '\n')

	val_file.close()
	train_file.close()


# rename val.txt from trainval2() -> test.txt; split train.txt into 80-20 for new train.txt and val.txt
def traintestval():
	os.rename(r'data/val.txt', r'data/test.txt')

	train_file = open('data/train.txt', 'r')
	training_imgs = train_file.readlines()
	train_file.close()

	list_size = len(training_imgs)
	train_size = int(0.8*list_size)

	random.shuffle(training_imgs)

	train_file = open('data/train.txt', 'w')
	for i in range(train_size):
		train_file.write(training_imgs[i])
	
	train_file.close()

	val_file = open('data/val.txt', 'w')

	for i in range(train_size, list_size):
		val_file.write(training_imgs[i])

	val_file.close()

traintestval()
# trainval2()
