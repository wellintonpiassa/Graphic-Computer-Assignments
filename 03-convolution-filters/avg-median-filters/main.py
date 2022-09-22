import cv2 as cv
import numpy as np
import math

# import image
img = cv.imread('example-image.jpg', cv.IMREAD_COLOR)
img_width = img.shape[0]
img_height = img.shape[1]

red_channel = img[:,:,2]
green_channel = img[:,:,1]
blue_channel = img[:,:,0]

# receiving neighbor number
print(f'Neighbor number: ')
neighbor = int(input())

# function with convolution algorithm
def convolution(filter_function):
    start = math.floor(neighbor/2)
    result_image = np.zeros(img.shape)

    for i in range(start, img_width - start):
        for j in range(start, img_height - start):
            red_frame = img[i-start:i+start+1, j-start:j+start+1, 2]
            green_frame = img[i-start:i+start+1, j-start:j+start+1, 1]
            blue_frame = img[i-start:i+start+1, j-start:j+start+1, 0]
            
            red_result = filter_function(red_frame)
            result_image[i][j][2] = red_result
            
            green_result = filter_function(green_frame)
            result_image[i][j][1] = green_result
            
            blue_result = filter_function(blue_frame)
            result_image[i][j][0] = blue_result

    stacked_imgs = np.hstack((img,result_image))
    cv.imwrite(f"{filter_function.__name__}_final_result.jpg", result_image)
    cv.imwrite(f"{filter_function.__name__}_stacked_images.jpg", stacked_imgs)

def avg_filter(frame):
    # somando media do frame
    return round(np.average(frame))

def median_filter(frame):
    # somando mediana do frame
    return round(np.median(frame))


convolution(avg_filter)
convolution(median_filter)
