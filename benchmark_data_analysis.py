import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.metrics import precision_score, recall_score, f1_score


def load_data():
    #root_dir = os.path.join(os.getcwd(), '../videos')

    root_dir = '/home/brandon/Projects/darknet/waste_data/combine videos/brandon + owen videos1/'
    file_name = os.path.join(root_dir, 'all_data.csv')
    data = []
    with open(file_name, 'r') as f:
        for line in f:
            data.append(line.split(','))

    def get_row_labels(col_num):
        # put min max labels in stats
        row_labels = []
        i = 0
        while i <len(data) and data[i][col_num] not in row_labels:
            if data[i][col_num] != '': row_labels.append(data[i][col_num])
            i += 1
        return row_labels

    dists = get_row_labels(0)
    stats = get_row_labels(1)
    data = [line[2:-1] for line in data]
    cams = [entry for entry in data[0] if entry != '']
    objs = [entry for entry in data[1] if entry != '']
    labels = [entry for entry in data[2] if entry != '']
    num_objs = len(set(objs))
    objs = objs[:num_objs]
    num_labels = len(set(labels))
    labels = labels[:num_labels]
    data = data[3:]

    data_categories = [stats, dists,labels,objs,cams]
    data = np.asarray(data).astype(np.float)
    # create a data tensor with dimension
    # min_max x distance x label x obj x cam_num
    data = np.stack(np.split(data, len(cams), axis=1), axis=0)
    data = np.stack(np.split(data, len(objs), axis=2), axis=0)
    data = np.stack(np.split(data, len(labels), axis=3), axis=0)
    data = np.stack(np.split(data, len(dists), axis=3), axis=0)
    data = np.stack(np.split(data, len(stats), axis=4), axis=0)
    print('stats: ' + str(stats))
    print('distance: ' + str(dists))
    print('labels: ' + str(labels))
    print('objs: ' + str(objs))
    print('cams: ' + str(cams))
    print('Shape corresponds to:  (stats , distance , label , obj , cam_num, 1, 1)')
    print(data.shape)
    return data, data_categories





data,data_categories = load_data()

np.delete(data, data[:,:,0,[1,2,4],:,:]) #delete irrelevant data
np.delete(data, data[:,:,1,[0,3],:,:]) #delete irrelevant data
np.delete(data, data[:,:,2,:,:,:], axis = 2) #remove person confidence data



title ="average mean object probability"
print(title)
category_num = 3 #obj
avg_prob = data[0] # 0 - mean, 1 - max
avg_prob = np.mean(avg_prob, axis=tuple([i for i in range(avg_prob.ndim) if i != category_num - 1]))
print(list(zip(data_categories[category_num], avg_prob)))
plt.title(title)
plt.xlabel = 'label'
plt.ylabel = 'probability'
plt.scatter(data_categories[category_num], avg_prob)
plt.show()

title ="average max object probability"
print(title)
avg_prob = data[1] # 0 - mean, 1 - max
avg_prob = np.mean(avg_prob, axis=tuple([i for i in range(avg_prob.ndim) if i != category_num - 1]))
print(list(zip(data_categories[category_num], avg_prob)))
plt.title(title)
plt.xlabel = 'label'
plt.ylabel = 'probability'
plt.scatter(data_categories[category_num], avg_prob)
plt.show()

title = "average mean distance vs probability"
print(title)
category_num = 1 #distance
avg_prob = data[0] # 0 - mean, 1 - max
avg_prob = np.mean(avg_prob, axis=tuple([i for i in range(avg_prob.ndim) if i != category_num - 1]))
print(list(zip(data_categories[category_num], avg_prob)))
plt.title(title)
plt.xlabel = 'distance'
plt.ylabel = 'probability'
plt.scatter(data_categories[category_num], avg_prob)
plt.show()

title="average max distance vs probability"
print(title)
category_num = 1 #distance
avg_prob = data[1] # 0 - mean, 1 - max
avg_prob = np.mean(avg_prob, axis=tuple([i for i in range(avg_prob.ndim) if i != category_num - 1]))
print(list(zip(data_categories[category_num], avg_prob)))
plt.title(title)
plt.xlabel = 'distance'
plt.ylabel = 'probability'
plt.scatter(data_categories[category_num], avg_prob)
plt.show()

title = "average mean camera vs probability"
print(title)
category_num = 4 # camera num
avg_prob = data[0] # 0 - mean, 1 - max
avg_prob = np.mean(avg_prob, axis=tuple([i for i in range(avg_prob.ndim) if i != category_num - 1]))
print(list(zip(data_categories[category_num], avg_prob)))
plt.title(title)
plt.xlabel = 'camera'
plt.ylabel = 'probability'
plt.scatter(data_categories[category_num], avg_prob)
plt.show()

title="average max camera vs probability"
print(title)
category_num = 4 #camera num
avg_prob = data[1] # 0 - mean, 1 - max
avg_prob = np.mean(avg_prob, axis=tuple([i for i in range(avg_prob.ndim) if i != category_num - 1]))
print(list(zip(data_categories[category_num], avg_prob)))
plt.title(title)
plt.xlabel = 'camera'
plt.ylabel = 'probability'
plt.scatter(data_categories[category_num], avg_prob)
plt.show()






