import cv2
import numpy as np
from matplotlib import pyplot as plt

# Importando imagem
img = cv2.imread('example-image.jpg', cv2.IMREAD_COLOR)

# Separando camadas e pegando dimensoes da imagem
img_width = img.shape[0]
img_height = img.shape[1]
img_channels = img.shape[2]

red_channel = img[:,:,2]
green_channel = img[:,:,1]
blue_channel = img[:,:,0]

# Criando e preechendo histograma
red_channel_histogram = np.zeros(256)
green_channel_histogram = np.zeros(256)
blue_channel_histogram = np.zeros(256)

for i in range(img_width):
    for j in range(img_height):
        pixel_value = red_channel[i][j]
        red_channel_histogram[pixel_value] = red_channel_histogram[pixel_value] + 1

        pixel_value = green_channel[i][j]
        green_channel_histogram[pixel_value] = green_channel_histogram[pixel_value] + 1
        
        pixel_value = blue_channel[i][j]
        blue_channel_histogram[pixel_value] = blue_channel_histogram[pixel_value] + 1


# Normalizando histograma
qtd_pixel = img_width * img_height
for i in range(len(red_channel_histogram)):
    red_channel_histogram[i] = red_channel_histogram[i] / qtd_pixel
    green_channel_histogram[i] = green_channel_histogram[i] / qtd_pixel
    blue_channel_histogram[i] = blue_channel_histogram[i] / qtd_pixel

#plt.bar(np.arange(len(red_channel_histogram)), red_channel_histogram)
#plt.show()

# Calculando função acumulada
red_channel_histogram_ac = np.cumsum(red_channel_histogram)
green_channel_histogram_ac = np.cumsum(green_channel_histogram)
blue_channel_histogram_ac = np.cumsum(blue_channel_histogram)

#plt.bar(np.arange(len(red_channel_histogram_ac)), red_channel_histogram_ac)
#plt.show()

# Criando a imagens resultante
img_eq = np.zeros(img.shape)
for i in range(img_width):
    for j in range(img_height):
        index = blue_channel[i][j]
        img_eq[i][j][0] = 255 * blue_channel_histogram_ac[index]
        index = green_channel[i][j]
        img_eq[i][j][1] = 255 * green_channel_histogram_ac[index]
        index = red_channel[i][j]
        img_eq[i][j][2] = 255 * red_channel_histogram_ac[index]

stacked_imgs = np.hstack((img,img_eq))
cv2.imwrite("equalized-image.jpg", img_eq)
cv2.imwrite("final-result.jpg", stacked_imgs)