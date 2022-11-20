import cv2 as cv
import statistics as s
import numpy as np


# importing image
img_name = "example-image.png"
img = cv.imread(img_name, 0)
img_width = img.shape[0]
img_height = img.shape[1]

def simple_global_thresholding():
    t = 128
    previous_t = 0
    delta_t = 0.2
    
    histogram = cv.calcHist(img, [0], None, [256], [0,256])
    
    while (abs(t - previous_t)) > delta_t:
        g1 = histogram.flatten()
        g2 = histogram.flatten()
        
        avg_g1 = np.average(np.arange(0, t, 1), weights=g1[0:t])
        avg_g2 = np.average(np.arange(t, 256, 1), weights=g2[t:256])
        previous_t = t
        t = round((avg_g1 + avg_g2) / 2)
    return t


def generating_new_image(t):
    result_img = np.zeros_like(img)
    
    for i in range(img_width):
        for j in range(img_height):
            if img[i][j] <= t:
                result_img[i][j] = 0
            else:
                result_img[i][j] = 255
                
    cv.imwrite(f"simples-{img_name}", result_img)


t = simple_global_thresholding()
print(f"t = {t}")
generating_new_image(t)       