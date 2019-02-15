import numpy as np
import cv2
import uuid
import os
from analyze_videos import *
import time
cwd = '/home/brandon/Projects/darknet/waste_data/videos/'
vid_len = 120
inp = '' 


def capture_video(num_cams):
    vid_len = 120   
    caps = [cv2.VideoCapture(i) for i in range(num_cams)]
    file_names =[os.path.join(cwd,'cam'+str(i)+'-'+str(uuid.uuid1())+'.avi') for i in range(num_cams)]
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    outs = [cv2.VideoWriter(file_names[i],fourcc, 20.0, (640,480)) for i in range(num_cams)]
    for i in range(vid_len):
        for j in range(num_cams):
            ret, frame = caps[j].read()
            if ret==True:
                frame = cv2.flip(frame,1)
                outs[j].write(frame)
                #cv2.imshow('frame',frame)
            else:
                break
    for i in range(num_cams):
        outs[i].release()
        caps[i].release()
    cv2.destroyAllWindows()
    return file_names

if __name__ == '__main__':
    setup_analyze()
    while inp != 'q':
        saved_file_names = capture_video(3)
        for fn in saved_file_names:
            analyze_video(fn)
        inp = raw_input('Hit enter ')

