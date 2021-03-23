import shutil
import os
import glob

# Current images folder contains both coordinates txt files and images, use this script to copy only images to the new folder

# Then perform image augmentation on this folder instead

source = './data/images/'
dest1 = './data/pic-only/'

files = os.listdir(source)

for pic in glob.glob(source+"*.jpg"):
    shutil.copy(pic, dest1);
