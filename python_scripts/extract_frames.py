from lxml import etree
import shutil
import os
import sys

""" 
Extract only annotated images from cvat XML download into new folder, and offset XML image count by 1.
""" 

video_name = sys.argv[1]

# downloaded annotations from cvat
# notes: on desktop
xml_path = "../final_annotations/" + video_name + "/" + video_name + ".xml"

# command to extract all frames from video:
# ffmpeg -i ~/Desktop/IoWT-New-Data/BinCam/GOPR1556.MP4 -start 0 -b:v 10000k -vsync 0 -an -y -q:v 16 ~/Desktop/images_BinCam2/%d.jpg
# notes: images_BinCam2 directory must exist before running command
# notes: on desktop

all_images_path = "../final_annotations/" + video_name + "/images_" + video_name + "/"

# directory must be created before running script
new_images_path = "../final_annotations/" + video_name + "/extracted_images_" + video_name

def extract_frames(video_name):
  tree = etree.parse(xml_path)
  root = tree.getroot() #import the data

  for object in root.iter("box"): # annotated frames have box labeling
      frame = int(object.get("frame"))
      #xmal frame matchs with images
      new_frame = frame + 1
      object.attrib['frame'] = str(new_frame)


      # check if box is not hidden
      if object.get("outside") != "1":
          #frame = int(object.get("frame")) # frame number
          # annotations are zero-indexed and expanded frames are 1-indexed
      

          frame = str(new_frame)
          frame += ".jpg"
          shutil.copy(os.path.join(all_images_path, frame), new_images_path)

  tree.write("../final_annotations/" + video_name + "/" + video_name + ".xml")

extract_frames(video_name)
