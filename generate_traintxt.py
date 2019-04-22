import os
def generate_train():
    dataset_dir = '/home/brandon/Projects/train_darknet/data/dataset-resized/dataset-resized/'
    classes = os.listdir(dataset_dir)
    data_dir = 'data/dataset-resized/dataset-resized/'
    image_path_lines = []
    for obj_class in classes:
        if '.' in obj_class: continue
        images = os.listdir(os.path.join(dataset_dir, obj_class))
        for image_name in images:
            if '.txt' in image_name: continue
            image_path_name = os.path.join(data_dir, obj_class+'/'+image_name)
            image_path_lines.append(image_path_name)
    traintxt_path = '/home/brandon/Projects/train_darknet/train.txt'
    with open(traintxt_path, 'a+') as f:
        f.writelines(image_path_lines)

if __name__ == '__main__':
    generate_train()

