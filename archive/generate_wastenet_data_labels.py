import os

def generate_waste_labels():
    root_dir = '/home/brandon/Projects/train_darknet/data/dataset-resized/dataset-resized'
    classes = os.listdir(root_dir)
    for i, class_name in enumerate(classes):
        if '.txt' in class_name: continue
        class_dir = os.path.join(root_dir,class_name)
        image_names = os.listdir(class_dir)
        for image_name in image_names:
            if '.txt' in image_names:continue
            image_file = os.path.join(class_dir, image_name)
            with open(image_file[:-4]+'.txt', 'w+') as f:
                write_str = str(i) +' 0.5 0.5 1.0 1.0 '
                f.write(write_str)
            train_file = os.path.join(root_dir, 'train.txt')
            with open(train_file, 'a+') as tf:
                tf.write(image_file + '\n')

if __name__ == '__main__':
    generate_waste_labels()
