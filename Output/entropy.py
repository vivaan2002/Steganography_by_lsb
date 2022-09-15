import numpy as np
import cv2

img1=cv2.imread('./png_new/lena.png')
img2=cv2.imread('./png_new/st_png.png')

marg1 = np.histogramdd(np.ravel(img1), bins = 256)[0]/img1.size
marg1 = list(filter(lambda p: p > 0, np.ravel(marg1)))
entropy1 = -np.sum(np.multiply(marg1, np.log2(marg1)))
ent_o="{:.4f}".format(entropy1)

marg2 = np.histogramdd(np.ravel(img2), bins = 256)[0]/img2.size
marg2 = list(filter(lambda p: p > 0, np.ravel(marg2)))
entropy2 = -np.sum(np.multiply(marg2, np.log2(marg2)))
ent_s="{:.4f}".format(entropy2)

print()
print("Entropy of original image is "+str(ent_o))
print("Entropy of new image is "+str(ent_s))
print()