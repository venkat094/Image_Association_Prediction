import cv2
import numpy as np
from matplotlib import pyplot as plt
from time import sleep
import time
import os
import imutils
import json

crop_image_path = r'C:\Users\Venkatraman.R\3D Objects\MAD_1\Test_Crop'
orig_image_path = r'C:\Users\Venkatraman.R\3D Objects\MAD_1\Test_original'
matched_image_path = r'C:\Users\Venkatraman.R\3D Objects\MAD_TASK_1_FINAL\matched_images'

for original in os.listdir(orig_image_path):
    for cropped in os.listdir(crop_image_path):
        original_file_path = os.path.join(orig_image_path,original)
        cropped_file_path = os.path.join(crop_image_path, cropped)
        # print ('original_image_file------>',original_file_path)
        # print ('Cropped_image_file------->',cropped_file_path)

        img_rgb = cv2.imread(original_file_path)
        template = cv2.imread(cropped_file_path)
        # img_rgb = cv2.resize(img_rgb,(700,700))
        # template = cv2.resize(template,(700,700))

        h1,w1 = template.shape[:2]
        # print ('template_shape',(h1,w1))
        # print ('Original_shape',img_rgb.shape)

        result = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)

        threshold = 0.7
        loc = np.where(result >= threshold)
        # print ('loc printing here----->',loc[1])
        # print ('length of the loc ---->',len(loc[1]))
        coordinates = 0
        if len(loc[1]) != 0:

            # TM_CCOEFF_NORMED
            (_, _, minLoc, maxLoc) = cv2.minMaxLoc(result)
            # print ((_, _, minLoc, maxLoc))
            # print (minLoc,maxLoc)

            topLeft = maxLoc
            botRight = (topLeft[0] + w1, topLeft[1] + h1)
            roi = img_rgb[topLeft[1]:botRight[1], topLeft[0]:botRight[0]]

            # print ('top Left------>',topLeft)
            # print ('bot right----->',botRight)

            coordinates = list(topLeft) + list (botRight)

            # print ('X1,Y1,X2,Y2 ------>',coordinates)

            # constructing a darkened transparent 'layer' to darken everything

            mask = np.zeros(img_rgb.shape, dtype = "uint8")
            img_rgb = cv2.addWeighted(img_rgb, 0.25, mask, 0.75, 0)

            # put the original  back in the image so that it is
            # 'brighter' than the rest of the image
            img_rgb[topLeft[1]:botRight[1], topLeft[0]:botRight[0]] = roi

            # display the images
            cv2.imshow("Design", imutils.resize(img_rgb, height = 650))

            crop_file_name = cropped_file_path.split('\\')[-1]
            # print ('crop_file_name------>',crop_file_name)

            original_file_name = original_file_path.split('\\')[-1]
            # print('original_file_name------>',original_file_name)

            # print ("Cropped File name with coordinates")

            mydict = {original_file_name : (crop_file_name,coordinates)}

            serialized = json.dumps(mydict, sort_keys=True, indent=3)

            print (serialized)

            # print (json.loads(serialized))

            matched_path = os.path.join(matched_image_path,crop_file_name)

            cv2.imwrite( matched_path, imutils.resize(img_rgb, height = 650))

            cv2.waitKey(0)

        else:
            # print ("this is not the one ")
            crop_file_name = cropped_file_path.split('\\')[-1]
            # print ('crop_file_name------>',crop_file_name)

            original_file_name = original_file_path.split('\\')[-1]
            # print('original_file_name------>',original_file_name)
            new1 = "# No Crop Association"

            mydict = {original_file_name : (crop_file_name,new1)}

            serialized = json.dumps(mydict, sort_keys=True, indent=3)

            print (serialized)