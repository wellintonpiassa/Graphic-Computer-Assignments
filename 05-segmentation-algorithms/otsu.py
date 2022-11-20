import cv2 as cv
import numpy as np

# importing image
img_name = "example-image.png"
img = cv.imread(img_name, 0)
img_width = img.shape[0]
img_height = img.shape[1]

def calculate_avg(hist, i, j, denominator):
    if denominator == 0: return 0
    x = [i for i in range(i, j+1)]
    x = np.asarray(x)
    avg = np.multiply(x, hist[i:j+1])
    avg = sum(avg) / denominator
    return avg

def calculate_histogram(img):
    histogram = np.zeros(256, dtype=float)
    for i in range(img_width):
        for j in range(img_height):
            histogram[img[i][j]] += 1
    histogram = histogram / sum(histogram)
    return histogram

def otsu():
    histogram = calculate_histogram(img)
    # calcultaing global pixel avg
    mg = 0
    for i in range(0, 256):
        mg = mg + i * histogram[i]
    
    h_variance = 0
    h_variance_t = 0
    
    for t in range(1,255):
        # calcultaing variance
        p1 = sum(histogram[0:t+1])
        p2 = 1 - p1
        m1 = calculate_avg(histogram, 0, t, p1)
        m2 = calculate_avg(histogram, t+1, 255, p2)
        current_variance = (p1 * ((m1-mg)**2)) + (p2*((m2-mg)**2))
        if h_variance < current_variance:
            h_variance = current_variance
            h_variance_t = t
    
    return h_variance_t


def generating_new_image(t):
    result_img = np.zeros_like(img)
    
    for i in range(img_width):
        for j in range(img_height):
            if img[i][j] <= t:
                result_img[i][j] = 0
            else:
                result_img[i][j] = 255
                
    cv.imwrite(f"otsu-{img_name}", result_img)


t = otsu()
print(f"t = {t}")
generating_new_image(t)     