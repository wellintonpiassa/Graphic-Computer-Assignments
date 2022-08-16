import cv2
import numpy as np
from matplotlib import pyplot as plt

# Importando imagem
img = cv2.imread('example-image.jpg', 0)
img_width = img.shape[0]
img_height = img.shape[1]
red_channel = img[:,:,2]
green_channel = img[:,:,1]
blue_channel = img[:,:,0]

# Criando e preechendo histograma
histogram = np.zeros(256)
for i in range(img_width):
    for j in range(img_height):
        pixel_value = img[i][j]
        histogram[pixel_value] = histogram[pixel_value] + 1

# Normalizando histograma
qtd_pixel = img_width * img_height
for i in range(len(histogram)):
    histogram[i] = histogram[i] / qtd_pixel

plt.bar(np.arange(len(histogram)), histogram)
plt.show()

# Calculando função acumulada
histogram_ac = np.cumsum(histogram)

plt.bar(np.arange(len(histogram_ac)), histogram_ac)
plt.show()

# Criando a imagem resultante
img_eq = np.zeros(img.shape)
for i in range(img_width):
    for j in range(img_height):
        index = img[i][j]
        img_eq[i][j] = 255 * histogram_ac[index]

stacked_imgs = np.hstack((img,img_eq))
cv2.imwrite("equalized-image.jpg", img_eq)
cv2.imwrite("final-result.jpg", stacked_imgs)