import os
import sys

test_imgs = 'data/test_fresh'
model = sys.argv[1] # ex: 'model1'

for img in os.listdir(test_imgs):

    # create output folder
    os.system('mkdir models/' + model + '/out_images')

    # run test command
    path = os.path.join(test_imgs, img)
    data = 'models/' + model + '/med_obj.data'
    cfg = 'models/' + model + '/med_obj.cfg'
    weights = 'models/' + model + '/weights/med_obj_best.weights'
    cmd = './darknet detector test ' + data + ' ' + cfg + ' ' + weights + ' -dont_show ' + path
    os.system(cmd)

    # save predictions.jpg to output folder
    img_name = img.split('.')[0]
    img_name += '_out.JPG'
    os.system('mv predictions.jpg ' + img_name)
    os.system('mv ' + img_name + ' models/' + model + '/out_images')
