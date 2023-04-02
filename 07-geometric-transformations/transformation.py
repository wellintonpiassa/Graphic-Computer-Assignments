import math
import numpy as np
import cv2 as cv

def get_matrix(operation, values:tuple):
    if operation == 'scale': return np.matrix(f"{values[0]} 0 0;0 {values[1]} 0;0 0 1")
    elif operation == 'shear': return np.matrix(f"1 {values[0]} 0;{values[1]} 1 0;0 0 1")
    elif operation == 'translation': return np.matrix(f"1 0 {values[0]};0 1 {values[1]};0 0 1")
    elif operation == 'rotate':
        radian = round(math.radians(values), 6)
        cos = round(math.cos(radian), 3)
        sin = round(math.sin(radian),3)
        return np.matrix(f"{cos} -{sin} 0;{sin} {cos} 0;0 0 1")
    elif operation == 'reflection':
        if values[0] == 'x': return np.matrix(f"1 0 0;0 -1 0;0 0 1")
        elif values[0] == 'y': return np.matrix(f"-1 0 0;0 1 0;0 0 1")
        elif values[0] == 'y=x': return np.matrix(f"0 1 0;1 0 0;0 0 1")
        elif values[0] == 'y=-x': return np.matrix(f"0 -1 0;-1 0 0;0 0 1")

def scale(scale_values, point):
    Sx, Sy = scale_values[0], scale_values[1]
    matrix = get_matrix('scale', (Sx,Sy))
    point = np.matrix(f"{point[0]}; {point[1]}; 1")
    new_points = np.dot(matrix, point)
    new_x, new_y = math.ceil(new_points[0].item()), math.ceil(new_points[1].item())
    return new_x, new_y

def rotate(degree, point):
    matrix = get_matrix('rotate', (degree))
    new_points = np.dot(matrix, point)
    new_x, new_y = math.ceil(new_points.item(0,0)), math.ceil(new_points.item(0,1))
    return new_x, new_y

def shear(shear_value, point):
    Kx, Ky = shear_value[0], shear_value[1]
    matrix = get_matrix('shear', (Kx, Ky))
    point = np.matrix(f"{point[0]}; {point[1]}; 1")
    new_points = np.dot(matrix, point)
    new_x, new_y = math.ceil(new_points[0].item()), math.ceil(new_points[1].item())
    return new_x, new_y

def reflection(axis, point):
    matrix = get_matrix('reflection', (axis))
    point = np.matrix(f"{point[0]}; {point[1]}; 1")
    new_points = np.dot(matrix, point)
    new_x, new_y = new_points[0].item(), new_points[1].item()
    return new_x, new_y

def translation(translate_values, point):
    Tx, Ty = translate_values[0], translate_values[1]
    matrix = get_matrix('translation', (Tx, Ty))
    point = np.matrix(f"{point[0]}; {point[1]}; 1")
    new_points = np.dot(matrix, point)
    new_x, new_y = new_points[0].item(), new_points[1].item()
    return new_x, new_y

def composed_matrix(operations, values, point):
    for i in range(len(operations)):
        op_matrix = get_matrix(operations[i], values[i])
        if i == 0: matrix_final = op_matrix
        else: matrix_final = np.dot(matrix_final, op_matrix)
    point = np.matrix(f"{point[0]}; {point[1]}; 1")
    new_points = np.dot(matrix_final, point)
    new_x, new_y = math.ceil(new_points[0].item()), math.ceil(new_points[1].item())
    return new_x, new_y

def convolute_image(img, function):
    out_img = np.zeros(img.shape)
    for i in range(img_width):
        for j in range(img_height):
            out_img[i][j] = function(img[i][j])
    return out_img

def change_image(img, function, *args):
    out_img = np.zeros(img.shape)
    for i in range(img_width):
        for j in range(img_height):
            new_x, new_y = function(*args, (i,j))
            if 0 < new_x < img_width and 0 < new_y < img_height:
                out_img[new_x][new_y] = img[i][j]
    return out_img
    

# Importando imagem
input_image = cv.imread('example.png', 0)
img_width, img_height = input_image.shape[0], input_image.shape[1]

# Translação
translated_image = change_image(input_image, translation, (60,30))
stacked_imgs = np.hstack((input_image, translated_image))
stacked_imgs = cv.imwrite('translated-result.png', stacked_imgs)

# Escala
scaled_image = change_image(input_image, scale, (0.5,0.5))
stacked_imgs = np.hstack((input_image, scaled_image))
stacked_imgs = cv.imwrite('scaled-result.png', stacked_imgs)

# Rotação
rotated_image = change_image(input_image, rotate, (45))
stacked_imgs = np.hstack((input_image, rotated_image))
stacked_imgs = cv.imwrite('rotated-result.png', stacked_imgs)

# Cisalhamento
shear_image = change_image(input_image, shear, (0.5,0.5))
stacked_imgs = np.hstack((input_image, shear_image))
stacked_imgs = cv.imwrite('shear-result.png', stacked_imgs)

# Reflexão
reflection_image = change_image(input_image, reflection, ('y=x'))
stacked_imgs = np.hstack((input_image, reflection_image))
stacked_imgs = cv.imwrite('reflection-result.png', stacked_imgs)

# Matriz Composta
altered_image = change_image(input_image, composed_matrix, ['translation', 'rotate'],[(60,30),(60)])
stacked_imgs = np.hstack((input_image, altered_image))
stacked_imgs = cv.imwrite('composed-result.png', stacked_imgs)
