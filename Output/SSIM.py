from skimage.metrics import structural_similarity as ssim
import argparse
import imutils
import cv2

imageA = cv2.imread("./jpg_new/lena.jpg")
imageB = cv2.imread("./jpg_new/st_jpg.png")

# 4. Convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# 5. Compute the Structural Similarity Index (SSIM) between the two
#    images, ensuring that the difference image is returned
(score, diff) = ssim(grayA, grayB, full=True)

print("\n SSIM: {} \n".format(score))