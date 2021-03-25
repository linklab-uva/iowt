import os
import sys
import json

dataset = sys.argv[1]
video = sys.argv[2]

"""
sudo code: 

width = width
height = height
create txt files for all frames in videos

for each annotation label
	for each frame on which the label exits
	convert each xy coordinate to yolo format
	add yolo format to txt file for that frame
"""

names = {
    'gloves': '0',
    'holster': '1',
    'knife': '2',
    'ligasure': '3',
    'stapler': '4',
    'suction': '5',
}

def convert_and_add(coord, frame, label):
    left = coord[0]['x']
    top = coord[0]['y']
    right = coord[1]['x']
    bottom = coord[1]['y']

    dw = 1.0 / width
    dh = 1.0 / height
    x = (left + right) / 2.0
    y = (top + bottom) / 2.0
    w = right - left
    h = bottom - top
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh

    label_id = names[label]

    ann = label_id + ' ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h)
    # print("created label for", label, 'on frame', frame+1, "and adding to file")
    add_to_file(ann, frame)

def add_to_file(ann, frame):
    if frame < 10:
        num = '00' + str(frame)
    elif frame < 100:
        num = '0' + str(frame)
    else:
        num = str(frame)

    filename = 'dataset/' + dataset + '/' + video + '/' + video + '_' + num + '.txt'

    if os.path.exists(filename):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not

    yolo_file = open(filename,append_write)
    yolo_file.write(ann + '\n')
    yolo_file.close()


with open('dataset/' + dataset + '/json_annotations/' + video + '.json') as f:
  json_ann = json.load(f)

height = json_ann['itemMetadata']['system']['height'] # ['ffmpeg']['height'] -- for videos
width = json_ann['itemMetadata']['system']['width'] # ['ffmpeg']['width'] -- for videos

for ann in json_ann['annotations']:
    first_frame = ann['metadata']['system']['frame']
    first_frame += 1
    first_coord = ann['coordinates']
    first_label = ann['label']
    convert_and_add(first_coord, first_frame, first_label)

    for snap in ann['metadata']['system']['snapshots_']:
        coord = snap['data']
        frame = snap['frame']
        frame += 1
        label = snap['label']
        convert_and_add(coord, frame, label)

