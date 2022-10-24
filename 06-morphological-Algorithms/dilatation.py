import cv2 as cv
import numpy as np
import math

# import image
img = cv.imread('example-image.jpg', 0)
img_width = img.shape[0]
img_height = img.shape[1]

# Receiving structure elements
print("Insert structuring elements")
print("1 - Line\n2 - Box\n3 - Disc\n4 - Cross\n") 
print("Ps. Enter the options separated by space")
options = input("input: ")
options = options.split(" ")

# Checking if options is valid
for i in range(len(options)):
    options[i] = int(options[i])
    if ((options[i] < 1) or (options[i] > 4)):
        print("Invalid option")
        exit()


# Receiving a neighbor value
print("Insert neighbor value")
neighbor_number = int(input("input: "))
center = math.floor(neighbor_number / 2)

# Checking if neighbor value is valid
if((neighbor_number <= 1) or (neighbor_number % 2 == 0)):
    print("Invalid neighbor value (valids: 3, 5, 7, 9, 11, ...)")
    exit()


# Mounting structuring element
def mount_structuring_element(structure_index):
    structure = np.zeros((neighbor_number, neighbor_number))

    if structure_index == 1: # line structure
        structure = np.zeros(neighbor_number)
        for i in range(center - 1, neighbor_number):
            structure[i] = 1

    elif structure_index == 2: # box structure
        structure = structure.fill(1)

    elif structure_index == 3: # Disc structure
        radius = center
        for i in range(len(structure[0])):
            for j in range(len(structure[1])):
                distance = math.dist([center, center], [i,j])
                if(distance <= radius):
                    structure[i][j] = 1

    elif structure_index == 4: # Cross structure
        for i in range(len(structure[0])):
            for j in range(len(structure[1])):
                if(i == center or j == center):
                    structure[i][j] = 1

    return structure


def apply_dilatation(frame, structure):
    pass


def convolution():
    start = center
    result_image = np.zeros(img.shape)
    stacked_imgs = img

    print("Processing...")
    
    for k in range(len(options)):
        structuring_element = mount_structuring_element(options[k])

        for i in range(start, img_width - start):
            for j in range(start, img_height - start):
                frame = img[i-start:i+start+1, j-start:j+start+1]
                result_image[i][j] = apply_dilatation(frame, structuring_element)

        
        stacked_imgs = np.hstack((stacked_imgs, result_image))
        # cv.imwrite(f"{mask_name}_final_result.jpg", result_image)
    
    cv.imwrite(f"all_stacked_images.jpg", stacked_imgs)
    print("Finish!")
