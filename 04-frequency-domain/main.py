import cv2 as cv
import numpy as np
import math

# import image
# img = cv.imread('example-image.jpg', cv.IMREAD_COLOR)

img = cv.imread('example_image_50x50.jpg')
#img = cv.imread('example_image_128x128.jpg')
# img = cv.imread('example_image_512x512.jpg')

img_width = img.shape[0]
img_height = img.shape[1]

# getting RGB channels individually
# red_channel = img[:,:,2]
# green_channel = img[:,:,1]
# blue_channel = img[:,:,0]

def cossenoDCT(x, i, N):
    return (math.cos(((2.0*x+1)*i*math.pi)/(2*N)))


def alfa(x, a1, a2):
    if x == 0:
        return a1
    else:
        return a2


def dct():
    print("Creating DCT...")
    output_image = np.zeros(img.shape)
    n = img_width
    m = img_height
    alfa1 = 1.0/math.sqrt(n)
    alfa2 = math.sqrt(2.0/n)

    for u in range(n):
        for v in range(m):
            soma = 0

            # calculating the sum 
            for x in range(n):
                for y in range(m):
                    soma += img[x][y] * cossenoDCT(x,u,n) * cossenoDCT(y,v,m)

            aux = alfa(u, alfa1, alfa2) * alfa(v, alfa1, alfa2) * soma
            output_image[u][v] = aux

    cv.imwrite(f"output_image_{img_width}x{img_height}.jpg", output_image)
    print("Finish DCT!")
    
    

def inverseDCT():
    pass

dct()