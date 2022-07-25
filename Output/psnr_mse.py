from math import log10, sqrt
import cv2
import numpy as np
  
def PSNR(original, new):
    mse = np.mean((original - new) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return [100,0]
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return [psnr,mse]
  
def main():
     original = cv2.imread("./tif/original_tif.tif")
     new = cv2.imread("./tif/stago_tif.tif", 1)
     value = PSNR(original, new)
     print()
     print(f"PSNR value is {value[0]} dB")
     print(f"MSE value is {value[1]} dB")
     print()
       
if __name__ == "__main__":
    main()