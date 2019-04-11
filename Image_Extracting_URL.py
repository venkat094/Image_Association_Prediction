import urllib.request
import requests
import os
errorCount=0

# localpath = r"C:\Users\Venkatraman.R\3D Objects\MAD_1"
file_list = r"C:\Users\Venkatraman.R\3D Objects\MAD_1\Crop_URLS\image_{0}.jpg"

with open(r'crops_url_list.txt', 'r+') as f:
    img_count = 1

    for each in f:
        print (each)
        urllib.request.urlretrieve(each)

        print("Please Wait.. it will take some time")

        try:
            urllib.request.urlretrieve(each,
                                       file_list.format(img_count))
            img_count += 1
        except IOError:
            errorCount += 1
            # Stop in case you reach 100 errors downloading images
            if errorCount > 100:
                break
            else:
                print ("File does not exist")

    print ("Done!")

