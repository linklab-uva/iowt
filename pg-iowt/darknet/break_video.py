# break video into images - save images to folder
# save all image names in folder to txt file
# run darknet command on txt file 

import os

video_dir = 'data/mock_or_vids'
videoNum = 1
mock_video = 'mock_or' + videoNum

for videofile in os.listdir(video_dir):
    if videofile == mock_video + '.MP4': # remove, do all vids at once
        os.system('mkdir ' + mock_video) # create folder titled with video name
        os.system('ffmpeg -i ' + mock_video + '.MP4 ' + mock_video + '/' + mock_video + '_%03d.png') # break video ito images and save to folder with video name
        os.system('ls ' + video_dir + mock_video + '/* -d > mock_or_vids/' + mock_video + '.txt') # get all files in folder and save to txt file
        os.system('./darknet detector test models/model5/med_obj.data models/model5/med_obj.cfg models/model5/weights/med_obj_best.weights -ext output -dont_show -out ' + mock_video + '_result.json < data/mock_or_vids/' + mock_video + '.txt') # run darknet command on txt file

