val = '../../data/val.txt'
val_out = '../../out_images.txt'

val_file = open(val, 'r')
val_out_file = open(val_out, 'a')

images = val_file.readlines()

for image in images:
	image_name = image.split('/')[2].split('.')[0] + '_out.jpg'
	val_out_file.write('data/out_images/' + image_name + '\n')

val_file.close()
val_out_file.close()
