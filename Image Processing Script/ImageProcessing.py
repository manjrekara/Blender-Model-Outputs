import numpy as np
import PIL
import os

#print('Pillow Version:', PIL.__version__)

from PIL import Image
from numpy import asarray
from matplotlib import image
from matplotlib import pyplot

#Load the image 
#Change directory as needed to test
pic = image.imread(r'C:\\School\\Senior\\Spring2021\\ECE4902\\Blender Outputs\\Waist Item Files\\Material Waist\\Image0004.png')

# convert image to numpy array
data = asarray(pic)

#print(data)
print("pic is type:", type(pic))
# summarize shape
print(data.shape)

pyplot.imshow(pic)
pyplot.show()

#Iterate through the folder and store each image array
Image_Dict = {}
for subdir, dirs, files in os.walk(r'C:\School\Senior\Fall2020\ECE 4901\Misc\BlenderImages'):
    for filename in files:
        filepath = subdir + os.sep + filename
        #print(filepath)
        picture = image.imread(filepath)
        # convert image to numpy array
        Image_Array = asarray(picture)
        Image_Dict[filename] = Image_Array

for key, value in Image_Dict.items():
    print("")
    print("")
    print(key, ' : ', value)

new_array = data

data[data == 0.2] = 0.7 #hat reflectivity
data[data == 0.4] = 1.1 #cloth reflectivity
data[data == 0.6] = 1.5 #shoes reflectivity
data[data == 1] = 1.8 #skin reflectivity
