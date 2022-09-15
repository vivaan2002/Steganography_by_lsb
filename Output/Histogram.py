import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('./png_new/st_png.png')
color = ('r','g','b')
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.title("Histogram Stago Image")
plt.legend(["Red Channel","Green Channel","Blue Channel"])
plt.xlabel("Frequency of Pixel")
plt.ylabel("Number of Pixel")
plt.show()