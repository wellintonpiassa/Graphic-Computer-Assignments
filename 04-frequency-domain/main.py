import cv2 as cv
import numpy as np
import math

# import image
input_img = cv.imread('example_image_50x50.jpg', 0)
# input_img = cv.imread('example_image_128x128.jpg', 0)
# input_img = cv.imread('example_image_512x512.jpg', 0)

# getting image sizes
n = input_img.shape[0]
m = input_img.shape[1]



def cossenoDCT(x, i, N):
    return (math.cos(((2.0*x+1)*i*math.pi)/(2*N)))


def alfa(x, N):
    if x == 0:
        return 1.0/math.sqrt(N)
    else:
        return math.sqrt(2.0/N)


def dct(img):
    print("Creating DCT...")
    
    frequency_domain_image = np.zeros((n,m))

    # normalyzing image
    img = img/255
    
    for u in range(n):
        for v in range(m):
            soma = 0

            # calculating the sum 
            for x in range(n):
                for y in range(m):
                    soma += img[x][y] * cossenoDCT(x,u,n) * cossenoDCT(y,v,m)

            frequency_domain_image[u][v] = alfa(u, n) * alfa(v, m) * soma

    print("Finish DCT!")
    return (frequency_domain_image * 255)
    
    
def inverseDCT(frequency_domain_image):
    print("Creating Inverse DCT...")

    frequency_domain_image = frequency_domain_image / 255
    inverse_image = np.zeros((n,m))

    for x in range(n):
        for y in range(m):
            soma = 0

            # calculating the sum 
            for u in range(n):
                for v in range(m):
                    soma += alfa(u, n) * alfa(v, m) * frequency_domain_image[u][v] * cossenoDCT(x,u,n) * cossenoDCT(y,v,m)

            inverse_image[x][y] = soma
    
    print("Finish Inverse DCT!")
    return (inverse_image * 255)


def low_pass_filter(frequency_domain_image, d0):
    low_pass_filter_image = np.zeros_like(frequency_domain_image)

    for u in range(0, d0+1):
        for v in range(0, d0+1):
            if math.dist([0, 0], [u, v]) <= d0:
                low_pass_filter_image[u, v] = frequency_domain_image[u, v]

    return low_pass_filter_image


def high_pass_filter(frequency_domain_image, d0):
    high_pass_filter_image = np.zeros_like(frequency_domain_image)

    for u in range(0, d0+1):
        for v in range(0, d0+1):
            if math.dist([0, 0], [u, v]) > d0:
                high_pass_filter_image[u, v] = frequency_domain_image[u, v]

    return high_pass_filter_image



# Calling functions
frequency_domain_image = dct(input_img)
inverse_image = inverseDCT(frequency_domain_image)
low_pass_filter_image = low_pass_filter(frequency_domain_image, 10)
high_pass_filter_image = high_pass_filter(frequency_domain_image, 10)


# Outputs images
cv.imwrite(f"frequency_domain_image_{n}x{m}.jpg", frequency_domain_image)
cv.imwrite(f"inverse_image_{n}x{m}.jpg", inverse_image)
cv.imwrite(f"low_pass_filter_image_{n}x{m}.jpg", low_pass_filter_image)
cv.imwrite(f"high_pass_filter_image_{n}x{m}.jpg", high_pass_filter_image)