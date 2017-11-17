# This program asks the name of an image from the user and then sets the color of the individual pixels to green

import matplotlib.pyplot as plt
import numpy as np


name = input("Enter the name of the image: ")

name1 = plt.imread(name)

img = name1.copy()

for i in range(img.shape[0]):
    
    for j in range(img.shape[1]):
        
        img[i,j,0] = 0
        img[i,j,2] = 0

plt.imshow(img)
plt.show()