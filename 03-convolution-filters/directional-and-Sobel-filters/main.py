import cv2 as cv
import numpy as np
import math

# Receiving parameters from user
print("Which mask do you want apply?")
print("1 - horizontal\n2 - Vertical\n3 - +45\n4 - -45\n5 - Laplace\n6 - Horizontal Sobel\n7 - Vertical Sober\n") 
print("Ps. Enter the options separated by space")
options = input("input: ")
options = options.split(" ")

# Checking if options is valid
for i in range(len(options)):
    options[i] = int(options[i])
    if (options[i] < 1) or (options[i] > 7):
        print("Invalid option")
        exit()

# setting neighbor number
neighbor = 3

# import image
img = cv.imread('example-image.jpg', cv.IMREAD_COLOR)
img_width = img.shape[0]
img_height = img.shape[1]

red_channel = img[:,:,2]
green_channel = img[:,:,1]
blue_channel = img[:,:,0]

# Defining masks matrix
masks = {
    "horizontal": np.array([[-0.5,-0.5,-0.5],[1,1,1], [-0.5,-0.5,-0.5]], np.float64),
    "vertical": np.array([[-0.5,1,-0.5],[-0.5,1,-0.5],[-0.5,1,-0.5]], np.float64),
    "+45": np.array([[-1,-1,2],[-1,2,-1],[2,-1,-1]], np.float64),
    "-45": np.array([[2,-1,-1],[-1,2,-1],[-1,-1,2]], np.float64),
    "laplace": np.array([[0,-1,0],[-1,4,-1],[0,-1,0]], np.float64),
    "horizontal-sobel": np.array([[-1,-2,-1],[0,0,0],[1,2,1]], np.float64),
    "vertical-sobel": np.array([[-1,0,1],[-2,0,2],[-1,0,1]], np.float64)
} 

# Relation option menu with mask
relation = {
    1: "horizontal",
    2: "vertical",
    3: "+45",
    4: "-45",
    5: "laplace",
    6: "horizontal-sobel",
    7: "vertical-sobel"
}

# function apllying mask
def apply_filter(mask, frame):
    sum = 0
    for i in range(len(frame)):
        for j in range(len(frame)):
            sum += frame[i][j] * mask[i][j]
            
    sum = abs(sum)
    if sum > 255:
        sum = 255     
    return sum


# function with convolution algorithm
def convolution():
    start = math.floor(neighbor/2)
    result_image = np.zeros(img.shape)
    stacked_imgs = img

    print("Processing...")
    
    for k in range(len(options)): 
        mask_name = relation[options[k]]
        mask = masks[mask_name]

        for i in range(start, img_width - start):
            for j in range(start, img_height - start):
                red_frame = img[i-start:i+start+1, j-start:j+start+1, 2]
                green_frame = img[i-start:i+start+1, j-start:j+start+1, 1]
                blue_frame = img[i-start:i+start+1, j-start:j+start+1, 0]

                red_result = apply_filter(mask, red_frame)
                result_image[i][j][2] = red_result

                green_result = apply_filter(mask, green_frame)
                result_image[i][j][1] = green_result
                
                blue_result = apply_filter(mask, blue_frame)
                result_image[i][j][0] = blue_result
        
        stacked_imgs = np.hstack((stacked_imgs, result_image))
        # cv.imwrite(f"{mask_name}_final_result.jpg", result_image)
    
    cv.imwrite(f"all_stacked_images.jpg", stacked_imgs)
    print("Finish!")


# Calling function
convolution()
