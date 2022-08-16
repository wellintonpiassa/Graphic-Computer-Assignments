import cv2
import numpy as np


# Carregando imagem
image_path = 'ceca-uel.jpg'
img = cv2.imread(image_path, cv2.IMREAD_COLOR) # constante para definir como RGB

# Printar imagem de input
#cv2.imshow("image", img) # Mostra a imagem
#cv2.waitKey(0)  # Mantém a imagem aberta

# Extraindo as tres camadas de cores
R = img[:,:,2]
G = img[:,:,1]
B = img[:,:,0]

# Printar printando as camadas de input
#cv2.imshow("R", R)
#cv2.imshow("G", G)
#cv2.imshow("B", B)
#cv2.waitKey(0)

image_matrix = img

def convert_rgb_to_cmyk(rgb_matrix):
    blue_channel = rgb_matrix[:,:,0]
    green_channel = rgb_matrix[:,:,1]
    red_channel = rgb_matrix[:,:,2]

    size = blue_channel.shape

    cyan_channel = np.zeros(size)
    magenta_channel = np.zeros(size)
    yellow_channel = np.zeros(size)
    
    for i in range(len(blue_channel)):
        for j in range(len(blue_channel[i])):
            r_norm = red_channel[i][j] / 255;
            g_norm = green_channel[i][j] / 255;
            b_norm = blue_channel[i][j] / 255;

            k = 1 - max(r_norm, g_norm, b_norm)
            
            # imagem totalmente preta
            if k == 1:
                c, m, y, k = 0

            c = (1 - r_norm - k) / (1 - k)
            m = (1 - g_norm - k) / (1 - k)
            y = (1 - b_norm - k) / (1 - k)

            # Salvando na nova matriz
            cyan_channel[i][j] = c * 255
            magenta_channel[i][j] = m * 255
            yellow_channel[i][j] = y * 255

    cv2.imwrite("cyan-channel.jpg", cyan_channel)
    cv2.imwrite("magenta-channel.jpg", magenta_channel)
    cv2.imwrite("yellow-channel.jpg", yellow_channel)

convert_rgb_to_cmyk(image_matrix)