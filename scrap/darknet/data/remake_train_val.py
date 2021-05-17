def replace(images, new_file):
	for image in images:
		pieces = image.split('/')
		new_file.write(pieces[0] + '/yolo-images/' + pieces[2])

val = 'val.txt'
train = 'train.txt'

val_file = open(val, 'r')
val_images = val_file.readlines()
val_file.close()
new_val_file = open('yolo-val.txt', 'w')

train_file = open(train, 'r')
train_images = train_file.readlines()
train_file.close()
new_train_file = open('yolo-train.txt', 'w')

replace(val_images, new_val_file)
replace(train_images, new_train_file)

new_val_file.close()
new_train_file.close()
